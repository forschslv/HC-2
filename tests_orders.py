from app import app, db, User, Product, Order

# Используем тестовую конфигурацию
app.config['TESTING'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

with app.app_context():
    db.create_all()

    # Создаем пользователей
    buyer = User(username='buyer1', role='buyer')
    buyer.set_password('pass')
    admin = User(username='admin1', role='admin')
    admin.set_password('pass')
    db.session.add_all([buyer, admin])
    db.session.commit()

    # Создаем товар
    p = Product(name='TestProduct', price=10.0, quantity=5)
    db.session.add(p)
    db.session.commit()

    client = app.test_client()

    # 1) Залогиниться как buyer и попытаться создать заказ с чужим именем
    with client.session_transaction() as sess:
        sess['user_id'] = buyer.id
    resp = client.post('/orders', data={'customer_name': 'attacker', 'product_id': p.id, 'quantity': 2}, follow_redirects=True)
    ords = Order.query.all()
    assert len(ords) == 1
    assert ords[0].customer_name == 'buyer1', 'buyer должен сохранять своё имя'

    # Очистим заказы
    Order.query.delete(); db.session.commit()

    # 2) Залогиниться как admin и указать имя клиента
    with client.session_transaction() as sess:
        sess['user_id'] = admin.id
    resp = client.post('/orders', data={'customer_name': 'someclient', 'product_id': p.id, 'quantity': 3}, follow_redirects=True)
    ords = Order.query.all()
    assert len(ords) == 1
    assert ords[0].customer_name == 'someclient', 'admin должен иметь возможность указать имя клиента'

print('Tests passed')

