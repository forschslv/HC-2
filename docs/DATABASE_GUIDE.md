# 🗄️ SQLAlchemy и Базы данных

## Инициализация

```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
```

## Создание моделей

```python
from datetime import datetime

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
```

## Типы данных

```python
db.Column(db.Integer)        # Целое число
db.Column(db.Float)          # Вещественное число
db.Column(db.String(100))    # Строка (макс 100)
db.Column(db.Text)           # Длинный текст
db.Column(db.Boolean)        # Булево значение
db.Column(db.DateTime)       # Дата и время
db.Column(db.Date)           # Только дата
db.Column(db.JSON)           # JSON данные
```

## CRUD операции

### Create (Создание)
```python
product = Product(name='Ноутбук', price=50000)
db.session.add(product)
db.session.commit()

# Массовое добавление
products = [
    Product(name='Мышь', price=1500),
    Product(name='Клавиатура', price=3000)
]
db.session.add_all(products)
db.session.commit()
```

### Read (Чтение)
```python
# Все записи
all_products = Product.query.all()

# По ID
product = Product.query.get(1)

# Первый результат фильтра
product = Product.query.filter_by(name='Ноутбук').first()

# Все результаты фильтра
products = Product.query.filter_by(active=True).all()

# С условиями
products = Product.query.filter(Product.price > 5000).all()

# Сортировка
products = Product.query.order_by(Product.price.desc()).all()

# Ограничение
products = Product.query.limit(10).all()

# Пропуск (для пагинации)
products = Product.query.offset(20).limit(10).all()
```

### Update (Обновление)
```python
product = Product.query.get(1)
product.price = 55000
db.session.commit()

# Массовое обновление
Product.query.filter(Product.price < 1000).update({Product.active: False})
db.session.commit()
```

### Delete (Удаление)
```python
product = Product.query.get(1)
db.session.delete(product)
db.session.commit()

# Массовое удаление
Product.query.filter(Product.quantity == 0).delete()
db.session.commit()
```

## Полезные запросы

```python
from sqlalchemy import func

# Подсчет
total = Product.query.count()

# Агрегирование
avg_price = db.session.query(func.avg(Product.price)).scalar()
max_price = db.session.query(func.max(Product.price)).scalar()
total_sum = db.session.query(func.sum(Product.price)).scalar()

# Группировка
from sqlalchemy import func
results = db.session.query(
    Product.category_id,
    func.count(Product.id).label('count')
).group_by(Product.category_id).all()
```

## Отношения между таблицами

### One-to-Many
```python
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    products = db.relationship('Product', backref='category')

class Product(db.Model):
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
```

## Обработка ошибок

```python
from sqlalchemy.exc import IntegrityError

try:
    product = Product(name='Товар', price=100)
    db.session.add(product)
    db.session.commit()
except IntegrityError as e:
    db.session.rollback()
    print(f'Ошибка БД: {e}')
except Exception as e:
    db.session.rollback()
    print(f'Неизвестная ошибка: {e}')
```

## Создание таблиц

```python
from app import app, db

# В Python shell
with app.app_context():
    db.create_all()
    print('Таблицы созданы')
```

