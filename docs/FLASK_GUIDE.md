# 🚀 Flask Гайд для начинающих

## Что такое Flask?
Flask — микрофреймворк для создания веб-приложений на Python. Легкий, гибкий и идеален для обучения.

## Основные концепции

### 1. Маршруты (Routes)

Маршруты — это URL-адреса в приложении.

```python
from flask import Flask

app = Flask(__name__)

# Самый простой маршрут
@app.route('/')
def index():
    return 'Привет, мир!'

# Маршрут с параметром
@app.route('/product/<int:product_id>')
def product_detail(product_id):
    return f'Товар ID: {product_id}'

# Маршрут с GET и POST методами
@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'POST':
        # Обработка формы
        return 'Данные получены'
    return 'Список товаров'
```

### 2. Шаблоны (Templates)

Шаблоны — это HTML-файлы, которые Flask заполняет данными.

```python
from flask import render_template

@app.route('/user/<name>')
def greet(name):
    return render_template('greeting.html', username=name)
```

**greeting.html:**
```html
<h1>Привет, {{ username }}!</h1>
```

### 3. Передача данных в шаблон

```python
@app.route('/dashboard')
def dashboard():
    data = {
        'title': 'Панель управления',
        'products': ['Товар1', 'Товар2', 'Товар3'],
        'count': 42
    }
    return render_template('dashboard.html', **data)
```

### 4. Работа с HTML-формами

**app.py:**
```python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Проверка учетных данных
        return f'Вы вошли как {username}'
    return render_template('login.html')
```

**login.html:**
```html
<form method="POST">
    <input type="text" name="username" placeholder="Логин" required>
    <input type="password" name="password" placeholder="Пароль" required>
    <button type="submit">Вход</button>
</form>
```

### 5. URL для статических файлов

```html
<!-- В шаблоне -->
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
<img src="{{ url_for('static', filename='images/logo.png') }}" alt="Логотип">
<script src="{{ url_for('static', filename='js/script.js') }}"></script>
```

### 6. Динамические ссылки

```html
<!-- Генерируем ссылку на конкретный товар -->
<a href="{{ url_for('product_detail', product_id=123) }}">
    Просмотр товара
</a>

<!-- Результат: /product/123 -->
```

## Работа с БД (SQLAlchemy)

### Создание моделей

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
```

### CRUD операции

```python
# Create (Создание)
new_product = Product(name='Новый товар', price=99.99)
db.session.add(new_product)
db.session.commit()

# Read (Чтение)
all_products = Product.query.all()
product = Product.query.get(1)
product = Product.query.filter_by(name='Товар1').first()

# Update (Обновление)
product = Product.query.get(1)
product.price = 150.00
db.session.commit()

# Delete (Удаление)
product = Product.query.get(1)
db.session.delete(product)
db.session.commit()
```

## JSON API

```python
from flask import jsonify

@app.route('/api/products')
def api_products():
    products = Product.query.all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'price': p.price
    } for p in products])
```

## Обработка ошибок

```python
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', 
                         error_code=404, 
                         error_message='Страница не найдена'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('error.html', 
                         error_code=500, 
                         error_message='Ошибка сервера'), 500
```

## Запуск приложения

```python
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
```

Затем откройте браузер и перейдите на `http://localhost:5000`

## Полезные советы

✅ **Делай:**
- Используй блупринты для организации кода
- Проверяй тип данных перед использованием
- Логируй ошибки для отладки
- Используй `render_template` для HTML

❌ **Не делай:**
- Не встраивай HTML в Python-строки
- Не используй `debug=True` в продакшене
- Не передавай необработанные данные в шаблон
- Не забывай про `db.session.commit()`

## Структура проекта

```
my_app/
├── app.py              # Главный файл приложения
├── requirements.txt    # Зависимости
├── templates/          # HTML шаблоны
│   ├── base.html
│   ├── index.html
│   └── product.html
├── static/             # Статические файлы
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
└── docs/              # Документация
```

