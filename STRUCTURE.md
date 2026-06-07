# 🏗️ СТРУКТУРА ПРОЕКТА FLASK

## Как читать этот документ

Этот файл объясняет, как устроено приложение и где находится каждый компонент.

## 📁 ПОЛНАЯ СТРУКТУРА

```
HC-2 (папка проекта)
│
├─ app.py                          # 🔴 ГЛАВНЫЙ ФАЙЛ - вся логика приложения
│                                   # 310+ строк кода
│                                   # Модели, маршруты, функции
│
├─ requirements.txt                # 📦 Зависимости для установки
│                                   # pip install -r requirements.txt
│
├─ README.md                        # 📖 Описание проекта для GitHub
│                                   # Что входит и как использовать
│
├─ INSTRUCTIONS.md                 # 🎓 Инструкция по использованию ⭐
│                                   # ЧИТАЙ ПЕРВЫМ!
│
├─ STRUCTURE.md                    # 🏗️ Этот файл (описание структуры)
│
├─ app_database.db                 # 💾 БД (создается автоматически)
│                                   # SQLite файл с товарами и заказами
│
├─ templates/                       # 📄 HTML ШАБЛОНЫ (7 файлов)
│  │
│  ├─ base.html                    # 📋 Базовый шаблон
│  │                                # Используется всеми страницами
│  │                                # Содержит: navbar, footer, структуру
│  │
│  ├─ index.html                   # 🏠 Главная страница
│  │                                # Интегральная панель с KPI
│  │                                # Карточки: товары, заказы, доход
│  │
│  ├─ products.html                # 📦 Страница товаров
│  │                                # Таблица со всеми товарами
│  │                                # Кнопка "Добавить товар"
│  │                                # Модальное окно для добавления
│  │
│  ├─ product_detail.html          # 🔍 Деталь одного товара
│  │                                # Информация: цена, количество
│  │                                # Рекомендуемые похожие товары
│  │
│  ├─ orders.html                  # 🛒 Страница заказов
│  │                                # Таблица со всеми заказами
│  │                                # Форма для создания нового
│  │                                # Статусы заказов
│  │
│  ├─ statistics.html              # 📊 Страница статистики
│  │                                # Карточки с метриками
│  │                                # Графики matplotlib
│  │
│  └─ error.html                   # ❌ Страница ошибок
│                                   # 404, 500 и другие
│
├─ static/                          # 🎨 СТАТИЧЕСКИЕ ФАЙЛЫ
│  │
│  ├─ css/                          # 🎨 СТИЛИ
│  │  └─ style.css                 # 100+ строк CSS
│  │                                # Кастомные стили поверх Bootstrap
│  │                                # Переменные, анимации, адаптив
│  │
│  ├─ js/                           # ⚙️ СКРИПТЫ
│  │  └─ script.js                 # JavaScript функции
│  │                                # Форматирование, уведомления
│  │                                # Bootstrap инициализация
│  │
│  └─ charts/                       # 📈 ГРАФИКИ (создаются автоматически)
│     └─ statistics.png            # Matplotlib графики
│
└─ docs/                            # 📚 ДОКУМЕНТАЦИЯ (9 гайдов)
   │
   ├─ QUICK_START.md               # 🚀 Начни с этого!
   │                                # Как установить и запустить
   │
   ├─ FLASK_GUIDE.md               # 🌐 Гайд по Flask
   │                                # Маршруты, шаблоны, формы
   │
   ├─ DATABASE_GUIDE.md            # 🗄️ Гайд по БД
   │                                # SQLAlchemy, CRUD операции
   │
   ├─ SQL_GUIDE.md                 # 📋 Гайд по SQL
   │                                # SELECT, WHERE, JOIN, GROUP BY
   │
   ├─ HTML_TEMPLATES_GUIDE.md      # 📄 Гайд по Jinja2
   │                                # Переменные, циклы, условия
   │
   ├─ CSS_GUIDE.md                 # 🎨 Гайд по CSS
   │                                # Селекторы, Box Model, Grid, Flexbox
   │
   ├─ BOOTSTRAP_GUIDE.md           # 🎯 Гайд по Bootstrap
   │                                # Grid, компоненты, утилиты
   │
   ├─ CSV_JSON_GUIDE.md            # 📦 Гайд по CSV/JSON
   │                                # Чтение, запись, экспорт
   │
   └─ MATPLOTLIB_GUIDE.md          # 📈 Гайд по Matplotlib
                                    # Графики, диаграммы
```

## 🔴 app.py - Главный файл

Это сердце приложения. Содержит:

### 1️⃣ Импорты (строки 1-10)
```python
from flask import Flask, render_template, request, ...
from flask_sqlalchemy import SQLAlchemy
import json, csv, matplotlib, ...
```

### 2️⃣ Инициализация (строки 12-20)
```python
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_database.db'
db = SQLAlchemy(app)
```

### 3️⃣ Модели БД (строки 22-60)
```python
class Product(db.Model):           # Товары
class Order(db.Model):             # Заказы
```

### 4️⃣ Маршруты (строки 70-300)
```python
@app.route('/')                    # Главная
@app.route('/products')            # Товары
@app.route('/orders')              # Заказы
@app.route('/statistics')          # Статистика
@app.route('/api/products')        # JSON API
@app.route('/export/products')     # CSV экспорт
# ... и другие
```

### 5️⃣ Вспомогательные функции (строки 250-280)
```python
def generate_charts()              # Создание графиков
def to_dict()                      # Преобразование в словарь
```

## 🌊 ЖИЗНЕННЫЙ ЦИКЛ ЗАПРОСА

Когда пользователь открывает страницу:

```
1. Браузер отправляет запрос
        ↓
2. Flask получает маршрут
        ↓
3. Находит соответствующую функцию в app.py
        ↓
4. Функция получает данные из БД
        ↓
5. Передает данные в HTML шаблон
        ↓
6. Jinja2 обрабатывает шаблон
        ↓
7. Bootstrap + CSS оформляет страницу
        ↓
8. JavaScript добавляет интерактивность
        ↓
9. Браузер показывает готовую страницу
```

## 📊 ВЗАИМОСВЯЗЬ КОМПОНЕНТОВ

```
app.py (ЛОГИКА)
   ↓
   ├─→ Product (МОДЕЛЬ)      ←── app_database.db (БД)
   ├─→ Order (МОДЕЛЬ)        ←── app_database.db (БД)
   │
   ├─→ render_template()
        ↓
        ├─→ base.html (СТРУКТУРА)
        │    ├─→ index.html
        │    ├─→ products.html  ←── static/css/style.css
        │    ├─→ orders.html    ←── static/js/script.js
        │    └─→ ...            ←── Bootstrap CDN
        │
        └─→ context (ДАННЫЕ)
             ├─→ products
             ├─→ orders
             └─→ statistics
```

## 🎯 МАРШРУТЫ И ИХ ФУНКЦИИ

| URL | Метод | Файл | Функция |
|-----|-------|------|---------|
| `/` | GET | templates/index.html | Главная панель |
| `/products` | GET | templates/products.html | Список товаров |
| `/products` | POST | app.py | Добавить товар |
| `/product/1` | GET | templates/product_detail.html | Деталь товара |
| `/orders` | GET | templates/orders.html | Список заказов |
| `/orders` | POST | app.py | Создать заказ |
| `/statistics` | GET | templates/statistics.html | Графики |
| `/api/products` | GET | JSON | API товары |
| `/api/orders` | GET | JSON | API заказы |
| `/export/products` | GET | CSV | Экспорт CSV |

## 💾 БД - app_database.db

SQLite база данных содержит 2 таблицы:

### Таблица: product
```
id (PK)  | name | description | price | quantity | created_at
---------|------|-------------|-------|----------|----------
1        | Ноут | Мощный      | 50000 | 5        | 2026-01-01
2        | Мышь | USB         | 1500  | 20       | 2026-01-02
```

### Таблица: order
```
id (PK) | customer_name | product_id (FK) | quantity | total_price | status | created_at
--------|---------------|-----------------|----------|-------------|--------|----------
1       | Иван          | 1               | 1        | 50000       | pending| 2026-01-05
2       | Петр          | 2               | 3        | 4500        | pending| 2026-01-06
```

## 🎨 CSS и JavaScript

### style.css (100+ строк)
- Переменные CSS (цвета, тени)
- Кастомные стили для карточек
- Анимации на hover
- Адаптивный дизайн
- Утилиты

### script.js
- Инициализация Bootstrap
- Функции форматирования (валюта, дата)
- Уведомления
- Валидация форм

## 📚 ДОКУМЕНТАЦИЯ

Всего 9 гайдов по разным технологиям:

```
docs/
├─ QUICK_START.md           👈 НАЧНИ ОТСЮДА
├─ FLASK_GUIDE.md
├─ DATABASE_GUIDE.md
├─ SQL_GUIDE.md
├─ HTML_TEMPLATES_GUIDE.md
├─ CSS_GUIDE.md
├─ BOOTSTRAP_GUIDE.md
├─ CSV_JSON_GUIDE.md
└─ MATPLOTLIB_GUIDE.md
```

## 🔄 ТИПИЧНЫЙ СЦЕНАРИЙ ИСПОЛЬЗОВАНИЯ

### Сценарий 1: Добавить товар

```
Пользователь кликает на "Добавить товар"
        ↓
Открывается модальное окно (HTML в templates/products.html)
        ↓
Заполняет форму (name, price, quantity)
        ↓
Нажимает "Добавить"
        ↓
HTML form отправляет POST запрос на /products
        ↓
app.py получает данные из request.form
        ↓
Создает объект Product
        ↓
Добавляет в db.session
        ↓
db.session.commit() сохраняет в app_database.db
        ↓
Перенаправляет на /products
        ↓
Страница обновляется, новый товар в таблице
```

### Сценарий 2: Получить JSON данные

```
Приложение делает fetch запрос на /api/products
        ↓
app.py получает маршрут
        ↓
Запрашивает Product.query.all()
        ↓
Преобразует в JSON с помощью jsonify()
        ↓
Возвращает JSON ответ
        ↓
Приложение получает JSON и использует данные
```

## 🚀 КАК РАСШИРИТЬ

Если нужно добавить новую функцию:

1. **Измени модель** в app.py (добавь поле в class Product/Order)
2. **Создай маршрут** (@app.route)
3. **Сделай шаблон** в templates/
4. **Добавь стили** в static/css/
5. **Обнови навигацию** в base.html

## 📋 ПОЛЕЗНЫЕ КОМАНДЫ

```bash
# Запустить приложение
python app.py

# Открыть Flask shell
flask shell

# Просмотреть БД
# Используй SQLiteStudio

# Установить зависимости
pip install -r requirements.txt

# Найти ошибки
python -m py_compile app.py
```

## 🎓 ОБУЧАЮЩИЙ ПОРЯДОК

1. Запусти приложение
2. Посмотри как оно работает
3. Прочитай QUICK_START.md
4. Посмотри на структуру app.py
5. Прочитай гайды по нужным технологиям
6. Добавь свою функцию
7. Тестируй и дебугь
8. Готово!

---

**Удачи в разработке! 🎉**

Если что-то не понимаешь — смотри документацию в `docs/`

