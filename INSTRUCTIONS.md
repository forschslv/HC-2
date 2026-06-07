# 🎓 ИНСТРУКЦИЯ ПО ИСПОЛЬЗОВАНИЮ ШАБЛОНА

## 📦 Что входит в шаблон?

Полный готовый Flask проект для хакатона с:

- ✅ **app.py** - полнофункциональное приложение (310+ строк)
- ✅ **7 HTML шаблонов** с Bootstrap 5
- ✅ **2 готовые модели БД** (Product, Order)
- ✅ **CSS и JavaScript** для интерактивности
- ✅ **10+ маршрутов** с обработкой данных
- ✅ **JSON API** для получения данных
- ✅ **Экспорт в CSV**
- ✅ **Графики Matplotlib**
- ✅ **9 подробных гайдов** по технологиям

## 🚀 НАЧАЛО РАБОТЫ

### Шаг 1: Установка зависимостей

```bash
pip install -r requirements.txt
```

Если pip не работает:
```bash
pip install --upgrade pip
pip install Flask==2.3.0 Flask-SQLAlchemy==3.0.0 matplotlib==3.7.0 pandas==2.0.0
```

### Шаг 2: Запуск приложения

```bash
python app.py
```

Вы должны увидеть:
```
 * Running on http://localhost:5000
```

### Шаг 3: Открой в браузере

Перейди на `http://localhost:5000`

Ты увидишь:
- Главную страницу с интегральной панелью
- Навигацию с 4 разделами
- Кнопки для добавления товаров и заказов

## 📚 ДОКУМЕНТАЦИЯ

Все гайды находятся в папке `docs/`:

1. **QUICK_START.md** ⭐ - Начни с этого!
2. **FLASK_GUIDE.md** - Как работает Flask
3. **DATABASE_GUIDE.md** - Работа с БД
4. **HTML_TEMPLATES_GUIDE.md** - Создание страниц
5. **BOOTSTRAP_GUIDE.md** - Оформление
6. **CSS_GUIDE.md** - Стили
7. **SQL_GUIDE.md** - SQL запросы
8. **CSV_JSON_GUIDE.md** - Экспорт данных
9. **MATPLOTLIB_GUIDE.md** - Графики

## 🛠️ ОСНОВНЫЕ ОПЕРАЦИИ

### Просмотреть список товаров

1. Нажми на "Товары" в меню
2. Увидишь таблицу с товарами

### Добавить новый товар

1. Нажми на "Товары" → "Добавить товар"
2. Заполни форму в модальном окне
3. Нажми "Добавить"

### Создать заказ

1. Перейди в "Заказы"
2. Нажми "Новый заказ"
3. Выбери товар и покупателя
4. Нажми "Создать"

### Посмотреть статистику

1. Нажми на "Статистика"
2. Увидишь графики, созданные автоматически

### Получить JSON данные

Открой в браузере:
```
http://localhost:5000/api/products
http://localhost:5000/api/orders
```

### Экспортировать в CSV

1. Перейди в "Заказы"
2. Нажми "Экспорт CSV"
3. Файл загрузится

## 🔄 КАК РАСШИРИТЬ ДЛЯ ХАКАТОНА

### Шаг 1: Добавить новое поле в модель

В `app.py` найди класс `Product`:

```python
class Product(db.Model):
    # ...существующие поля...
    discount = db.Column(db.Float, default=0)  # Добавить это
```

Пересоздай БД:
```bash
rm app_database.db
python -c "from app import app, db; db.create_all()"
```

### Шаг 2: Добавить новый маршрут

В `app.py` добавь:

```python
@app.route('/my-page')
def my_page():
    products = Product.query.all()
    return render_template('my_page.html', products=products)
```

### Шаг 3: Создать новый HTML шаблон

Создай файл `templates/my_page.html`:

```html
{% extends "base.html" %}
{% block title %}Моя страница{% endblock %}
{% block content %}
    <h1>Список товаров</h1>
    <ul>
    {% for product in products %}
        <li>{{ product.name }} - {{ product.price }} ₽</li>
    {% endfor %}
    </ul>
{% endblock %}
```

### Шаг 4: Добавить кнопку в навигацию

В `templates/base.html` найди `<ul class="navbar-nav ms-auto">` и добавь:

```html
<li class="nav-item">
    <a class="nav-link" href="{{ url_for('my_page') }}">Моя страница</a>
</li>
```

### Шаг 5: Добавить стили

В `static/css/style.css` добавь:

```css
.my-custom-style {
    background-color: #f0f0f0;
    border-radius: 8px;
    padding: 20px;
}
```

## 💻 ПРИМЕРЫ КОДА

### Получить все товары из БД

```python
from app import app, Product

with app.app_context():
    products = Product.query.all()
    for p in products:
        print(f'{p.name}: {p.price} ₽')
```

### Найти товар по названию

```python
with app.app_context():
    product = Product.query.filter_by(name='Ноутбук').first()
    print(product.price)
```

### Обновить товар

```python
with app.app_context():
    product = Product.query.get(1)
    product.price = 60000
    db.session.commit()
```

### Удалить товар

```python
with app.app_context():
    product = Product.query.get(1)
    db.session.delete(product)
    db.session.commit()
```

### Работать с JSON

```python
import json

data = {'products': [{'id': 1, 'name': 'Товар1', 'price': 100}]}
with open('data.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

## 🐛 РЕШЕНИЕ ПРОБЛЕМ

### Проблема: "ModuleNotFoundError: No module named 'flask'"

**Решение:**
```bash
pip install -r requirements.txt
```

### Проблема: "Address already in use"

**Решение:** Порт 5000 уже занят. В `app.py` измени:
```python
app.run(port=5001)  # Используй другой порт
```

### Проблема: "database is locked"

**Решение:** Удали БД и пересоздай:
```bash
rm app_database.db
python app.py
```

### Проблема: "Template not found"

**Решение:** Проверь, что шаблон лежит в папке `templates/` с правильным названием

## 📋 ФАЙЛЫ И ИХ НАЗНАЧЕНИЕ

| Файл | Назначение |
|------|-----------|
| `app.py` | Главное приложение |
| `requirements.txt` | Список зависимостей |
| `templates/base.html` | Базовый шаблон |
| `templates/index.html` | Главная страница |
| `templates/products.html` | Страница товаров |
| `templates/orders.html` | Страница заказов |
| `templates/statistics.html` | Страница статистики |
| `static/css/style.css` | Основные стили |
| `static/js/script.js` | JavaScript функции |
| `docs/` | 9 подробных гайдов |
| `README.md` | Описание проекта |

## ✅ КОНТРОЛЬНЫЙ СПИСОК ПЕРЕД СДАЧЕЙ

- [ ] Приложение запускается без ошибок
- [ ] Все страницы открываются
- [ ] Можно добавлять товары и заказы
- [ ] Статистика показывает графики
- [ ] JSON API работает
- [ ] CSV экспорт работает
- [ ] Код документирован
- [ ] Нет ошибок в консоли
- [ ] Приложение адаптивное (работает на мобильных)
- [ ] Готово к представлению!

## 🎯 СТРУКТУРА ДЛЯ ХАКАТОНА

Рекомендуемая структура для твоего хакатона:

```
my-hackathon-project/
├── app.py              # Твой основной код
├── requirements.txt    # Твои зависимости
├── templates/          # Твои HTML страницы
├── static/             # Твои стили и скрипты
├── docs/               # Документация
├── README.md           # Описание проекта
└── presentations/      # Презентация и фото
```

## 🚀 РАЗВЕРТЫВАНИЕ НА ХОСТИНГ

### На Heroku (бесплатно)

1. Создай аккаунт на heroku.com
2. Установи Heroku CLI
3. В проекте создай `Procfile`:
```
web: gunicorn app:app
```

4. Запусти:
```bash
heroku login
heroku create my-app
git push heroku main
```

### На PythonAnywhere (бесплатно)

1. Создай аккаунт на pythonanywhere.com
2. Загрузи файлы
3. Настрой WSGI конфигурацию
4. Запусти приложение

## 📞 ЧАСТЫЕ ВОПРОСЫ

**Q: Как изменить название приложения?**  
A: В `app.py` измени значение переменной в navbar

**Q: Как добавить больше полей в форму?**  
A: Добавь поля в модель, HTML форму и обработку в маршруте

**Q: Как сменить цветовую схему?**  
A: В `static/css/style.css` измени цвета в переменных `:root`

**Q: Как добавить аутентификацию?**  
A: Используй Flask-Login, хотя для хакатона часто не требуется

**Q: Как оптимизировать производительность?**  
A: Используй кэширование и оптимизируй SQL запросы

## 🎉 ГОТОВО!

Теперь у тебя есть:
- ✅ Полностью функциональное Flask приложение
- ✅ Красивый и адаптивный дизайн
- ✅ Работающая БД с примерами
- ✅ API для интеграций
- ✅ Полная документация

**Успехов на хакатоне! 🏆**

Если остались вопросы — смотри документацию в папке `docs/`

