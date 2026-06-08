from app import app, db, User, Product, Order

app.config['TESTING'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

with app.app_context():
    # Очистим (на случай существующих данных) и создадим таблицы заново
    db.drop_all()
    db.create_all()
    buyer = User(username='buyer1', role='buyer')
    buyer.set_password('pass')
    admin = User(username='admin1', role='admin')
    admin.set_password('pass')
    db.session.add_all([buyer, admin])
    db.session.commit()
    p = Product(name='TestProduct', price=10.0, quantity=5)
    db.session.add(p)
    db.session.commit()

    client = app.test_client()

    with client.session_transaction() as sess:
        sess['user_id'] = buyer.id
    resp = client.post('/orders', data={'customer_name': 'attacker', 'product_id': p.id, 'quantity': 2}, follow_redirects=True)
    print('Response status code:', resp.status_code)
    print('Response location/history length:', len(resp.history) if hasattr(resp, 'history') else 'no history')
    ords = Order.query.all()
    print('Orders after buyer post:', [(o.id, o.customer_name, o.product_id, o.quantity) for o in ords])

    Order.query.delete(); db.session.commit()

    with client.session_transaction() as sess:
        sess['user_id'] = admin.id
    resp = client.post('/orders', data={'customer_name': 'someclient', 'product_id': p.id, 'quantity': 3}, follow_redirects=True)
    ords = Order.query.all()
    print('Orders after admin post:', [(o.id, o.customer_name, o.product_id, o.quantity) for o in ords])

print('Done')
