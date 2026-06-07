# 📋 README - Шаблон приложения для хакатона

## 🎯 Описание

Универсальный шаблон Flask приложения для хакатона. Включает все необходимые компоненты:

✅ **Backend:** Flask + SQLAlchemy  
✅ **Frontend:** HTML/CSS/JavaScript + Bootstrap 5  
✅ **БД:** SQLite с готовыми моделями  
✅ **API:** JSON endpoints  
✅ **Экспорт:** CSV и JSON  
✅ **Графики:** Matplotlib с примерами  
✅ **Документация:** 9 подробных гайдов  

## 📚 Документация

В папке `docs/` находятся 9 гайдов для разных технологий:

1. **QUICK_START.md** - Начни отсюда! 🚀
2. **SQL_GUIDE.md** - SQL запросы и БД
3. **FLASK_GUIDE.md** - Основы Flask
4. **HTML_TEMPLATES_GUIDE.md** - Jinja2 шаблоны
5. **CSS_GUIDE.md** - Стили и оформление
6. **BOOTSTRAP_GUIDE.md** - Bootstrap компоненты
7. **CSV_JSON_GUIDE.md** - Работа с данными
8. **MATPLOTLIB_GUIDE.md** - Графики и диаграммы
9. **DATABASE_GUIDE.md** - SQLAlchemy и SQLite

## 🚀 Быстрый старт

```bash
# Установка
pip install -r requirements.txt

# Запуск
python app.py

# Откройте http://localhost:5000
```

## 📁 Структура

```
HC-2/
├── app.py                    # Главное приложение (310+ строк кода)
├── requirements.txt          # Зависимости
├── app_database.db          # БД (создается автоматически)
├── templates/               # 6 HTML шаблонов
│   ├── base.html           # Базовый шаблон
│   ├── index.html          # Главная страница
│   ├── products.html       # Список товаров
│   ├── product_detail.html # Детали товара
│   ├── orders.html         # Заказы
│   ├── statistics.html     # Статистика
│   └── error.html          # Страница ошибок
├── static/                  # Статические файлы
│   ├── css/
│   │   └── style.css       # Основные стили (100+ строк)
│   ├── js/
│   │   └── script.js       # Вспомогательные функции
│   └── charts/             # Графики (создаются автоматически)
└── docs/                    # Подробная документация
    ├── QUICK_START.md
    ├── SQL_GUIDE.md
    ├── FLASK_GUIDE.md
    ├── HTML_TEMPLATES_GUIDE.md
    ├── CSS_GUIDE.md
    ├── BOOTSTRAP_GUIDE.md
    ├── CSV_JSON_GUIDE.md
    ├── MATPLOTLIB_GUIDE.md
    ├── DATABASE_GUIDE.md
    └── README.md (этот файл)
```

## 🎨 Особенности

### Backend (app.py)
- **2 модели БД:** Product и Order
- **10+ маршрутов:** для работы с товарами, заказами, статистикой
- **JSON API:** для получения данных в формате JSON
- **Экспорт:** в CSV формате
- **Графики:** автоматическая генерация matplotlib графиков
- **Обработка ошибок:** 404 и 500 страницы

### Frontend
- **6 HTML шаблонов** с использованием Jinja2
- **Bootstrap 5** для адаптивного дизайна
- **Модальные окна** для добавления/редактирования данных
- **Адаптивная верстка** для мобильных и ПК
- **Таблицы, формы, карточки** - все готово

### БД
- **SQLite** - встроенная, не требует настройки
- **SQLAlchemy ORM** - для удобной работы с данными
- **Отношения между таблицами** - ready to use
- **Автоматические временные метки** - created_at, updated_at

## 📌 Готовые функции

| Функция | Маршрут | Описание |
|---------|---------|---------|
| Главная | GET / | Интегральная панель с статистикой |
| Товары | GET /products | Список всех товаров |
| Добавить товар | POST /products | Через модальное окно |
| Деталь товара | GET /product/<id> | Информация о конкретном товаре |
| Заказы | GET /orders | Список заказов |
| Создать заказ | POST /orders | Новый заказ через форму |
| Статистика | GET /statistics | Графики и КПЭ |
| JSON товары | GET /api/products | API endpoint |
| JSON заказы | GET /api/orders | API endpoint |
| Экспорт CSV | GET /export/products | Скачивание данных |

## 🔧 Примеры кода

### Добавить новый товар
```python
from app import Product, db, app

with app.app_context():
    product = Product(
        name='Ноутбук',
        price=50000,
        quantity=5
    )
    db.session.add(product)
    db.session.commit()
    print(f'Товар создан: {product.id}')
```

### Создать новый маршрут
```python
@app.route('/my-page')
def my_page():
    products = Product.query.all()
    return render_template('my_page.html', products=products)
```

### Новый HTML шаблон
```html
{% extends "base.html" %}
{% block title %}Моя страница{% endblock %}
{% block content %}
    <h1>{{ page_title }}</h1>
    {% for item in items %}
        <p>{{ item }}</p>
    {% endfor %}
{% endblock %}
```

## 🎯 Использование для хакатона

1. **Копируй** этот шаблон как основу
2. **Измени модели** Product и Order под свою задачу
3. **Добавь новые маршруты** для функционала
4. **Создай HTML шаблоны** для новых страниц
5. **Оформи** Bootstrap классами
6. **Добавь логику** обработки данных
7. **Тестируй** и дебугь
8. **Готово!** Шаблон готов к представлению

## 🛠️ Технологический стек

| Слой | Технология | Версия |
|------|-----------|--------|
| Backend | Flask | 2.3.0 |
| ORM | SQLAlchemy | 3.0.0 |
| БД | SQLite | - |
| Frontend | HTML5/CSS3/JS | - |
| CSS Framework | Bootstrap | 5.3.0 |
| Графики | Matplotlib | 3.7.0 |
| Шаблоны | Jinja2 | встроена |

## 🐛 Решение проблем

### БД не создается
```bash
python
>>> from app import app, db
>>> with app.app_context():
...     db.create_all()
>>> exit()
```

### Порт 5000 занят
В app.py измени: `app.run(port=5001)`

### Модули не устанавливаются
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 📖 Рекомендуемый порядок изучения

1. **QUICK_START.md** - Запусти приложение
2. **FLASK_GUIDE.md** - Поймите структуру
3. **DATABASE_GUIDE.md** - Работа с БД
4. **HTML_TEMPLATES_GUIDE.md** - Создание страниц
5. **BOOTSTRAP_GUIDE.md** - Оформление
6. **SQL_GUIDE.md** - Запросы к БД
7. **CSV_JSON_GUIDE.md** - Экспорт данных
8. **MATPLOTLIB_GUIDE.md** - Графики
9. **CSS_GUIDE.md** - Продвинутые стили

## 🎓 Что вы изучите

✅ Создание веб-приложений на Flask  
✅ Работа с базами данных SQLite  
✅ ORM и SQLAlchemy  
✅ HTML шаблоны и Jinja2  
✅ HTML формы и обработка данных  
✅ CSS и оформление  
✅ Bootstrap компоненты  
✅ JSON API  
✅ CSV экспорт/импорт  
✅ Matplotlib графики  
✅ SQL запросы  

## 🚀 Развертывание

### На Heroku
```bash
git init
git add .
git commit -m "Initial commit"
heroku create my-app
git push heroku main
```

### На PythonAnywhere
1. Залей файлы на сервер
2. Создай Web app
3. Установи зависимости
4. Запусти приложение

## 📞 Поддержка

Для вопросов обратитесь к документации в `docs/`

## 📝 Лицензия

Свободно используется в учебных и коммерческих целях

---

**Создано для хакатона 2026**  
**Удачи в разработке! 🎉**

