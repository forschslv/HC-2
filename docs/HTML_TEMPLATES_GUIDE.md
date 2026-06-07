до# 📄 HTML Шаблоны и Jinja2 Гайд

## Основы Jinja2

Jinja2 — это язык шаблонизации, который Flask использует для создания динамического HTML.

## 1. Переменные

### Вывод переменной
```html
<!-- В Python: render_template('page.html', name='Иван') -->
<h1>Привет, {{ name }}!</h1>
<!-- Результат: <h1>Привет, Иван!</h1> -->
```

### Фильтры
```html
<!-- Большие буквы -->
<p>{{ name|upper }}</p>

<!-- Маленькие буквы -->
<p>{{ name|lower }}</p>

<!-- Первая буква большая -->
<p>{{ name|capitalize }}</p>

<!-- Форматирование чисел -->
<p>{{ price|round(2) }}</p>

<!-- Длина строки -->
<p>{{ text|length }}</p>

<!-- Случайный выбор -->
<p>{{ items|random }}</p>
```

## 2. Условия (if/else)

```html
<!-- Простое условие -->
{% if user %}
    <p>Пользователь: {{ user.name }}</p>
{% endif %}

<!-- if/else -->
{% if age >= 18 %}
    <p>Вы взрослый</p>
{% else %}
    <p>Вы несовершеннолетний</p>
{% endif %}

<!-- if/elif/else -->
{% if score >= 90 %}
    <p>Отличный результат!</p>
{% elif score >= 70 %}
    <p>Хороший результат</p>
{% elif score >= 50 %}
    <p>Пройдено</p>
{% else %}
    <p>Не пройдено</p>
{% endif %}

<!-- Логические операторы -->
{% if user and user.is_admin %}
    <p>Это администратор</p>
{% endif %}

{% if status == 'active' or status == 'pending' %}
    <p>Статус активен</p>
{% endif %}
```

## 3. Циклы (for)

```html
<!-- Простой цикл -->
<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>

<!-- С индексом (начинается с 1) -->
<ul>
{% for item in items %}
    <li>{{ loop.index }}. {{ item }}</li>
{% endfor %}
</ul>

<!-- С доступом к первому и последнему -->
<ul>
{% for item in items %}
    <li>
        {{ item }}
        {% if loop.first %} (первый){% endif %}
        {% if loop.last %} (последний){% endif %}
    </li>
{% endfor %}
</ul>

<!-- Проверка на четность -->
<ul>
{% for item in items %}
    <li class="{% if loop.index is odd %}odd{% else %}even{% endif %}">
        {{ item }}
    </li>
{% endfor %}
</ul>

<!-- Цикл else (если список пуст) -->
<ul>
{% for product in products %}
    <li>{{ product.name }}</li>
{% else %}
    <li>Товары не найдены</li>
{% endfor %}
</ul>
```

## 4. Вложенные циклы

```html
<table>
{% for user in users %}
    <tr>
        <td>{{ user.name }}</td>
        <td>
            <ul>
            {% for order in user.orders %}
                <li>{{ order.id }} - {{ order.status }}</li>
            {% endfor %}
            </ul>
        </td>
    </tr>
{% endfor %}
</table>
```

## 5. Наследование шаблонов

### base.html (базовый шаблон)
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Мое приложение{% endblock %}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <nav>
        <a href="/">Главная</a>
        <a href="/about">О сайте</a>
    </nav>

    <div class="container">
        {% block content %}
            <!-- Контент переопределяется в дочерних шаблонах -->
        {% endblock %}
    </div>

    <footer>
        <p>&copy; 2026</p>
    </footer>
</body>
</html>
```

### products.html (дочерний шаблон)
```html
{% extends "base.html" %}

{% block title %}Товары - Мое приложение{% endblock %}

{% block content %}
    <h1>Список товаров</h1>
    <ul>
    {% for product in products %}
        <li>{{ product.name }} - {{ product.price }} ₽</li>
    {% endfor %}
    </ul>
{% endblock %}
```

## 6. Включение других шаблонов

```html
<!-- Вставить содержимое другого шаблона -->
{% include 'components/header.html' %}

<main>
    <!-- Основное содержимое -->
</main>

{% include 'components/footer.html' %}
```

### components/header.html
```html
<header>
    <h1>Мой сайт</h1>
    <nav>
        <a href="/">Главная</a>
        <a href="/products">Товары</a>
    </nav>
</header>
```

## 7. URL и статические файлы

```html
<!-- Ссылка на маршрут -->
<a href="{{ url_for('index') }}">Главная</a>

<!-- Ссылка с параметром -->
<a href="{{ url_for('product_detail', product_id=123) }}">Товар #123</a>

<!-- Статические файлы -->
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
<img src="{{ url_for('static', filename='images/logo.png') }}" alt="Логотип">
<script src="{{ url_for('static', filename='js/script.js') }}"></script>
```

## 8. Формы

```html
<!-- Простая форма -->
<form method="POST" action="{{ url_for('add_product') }}">
    <label for="name">Название:</label>
    <input type="text" id="name" name="name" required>

    <label for="price">Цена:</label>
    <input type="number" id="price" name="price" step="0.01" required>

    <button type="submit">Добавить</button>
</form>

<!-- Форма с выбором -->
<form method="POST">
    <select name="category">
        {% for cat in categories %}
            <option value="{{ cat.id }}">{{ cat.name }}</option>
        {% endfor %}
    </select>
</form>

<!-- Форма с галочками -->
<form method="POST">
    {% for tag in tags %}
        <label>
            <input type="checkbox" name="tags" value="{{ tag.id }}">
            {{ tag.name }}
        </label>
    {% endfor %}
</form>
```

## 9. Макросы (переиспользуемые блоки кода)

```html
<!-- Определение макроса -->
{% macro render_product(product) %}
    <div class="product-card">
        <h3>{{ product.name }}</h3>
        <p>Цена: {{ product.price }} ₽</p>
        <p>Количество: {{ product.quantity }}</p>
    </div>
{% endmacro %}

<!-- Использование макроса -->
{% for product in products %}
    {{ render_product(product) }}
{% endfor %}
```

## 10. Комментарии

```html
<!-- HTML комментарий (виден в исходнике) -->
{# Комментарий Jinja2 (не виден в исходнике) #}

<!-- Многострочный комментарий -->
{% comment %}
    Это длинный комментарий
    который может занимать несколько строк
{% endcomment %}
```

## 11. Практические примеры

### Таблица товаров
```html
<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Название</th>
            <th>Цена</th>
            <th>Действие</th>
        </tr>
    </thead>
    <tbody>
    {% for product in products %}
        <tr>
            <td>{{ product.id }}</td>
            <td>{{ product.name }}</td>
            <td>{{ "%.2f"|format(product.price) }} ₽</td>
            <td>
                <a href="{{ url_for('edit_product', id=product.id) }}">Редактировать</a>
                <a href="{{ url_for('delete_product', id=product.id) }}">Удалить</a>
            </td>
        </tr>
    {% endfor %}
    </tbody>
</table>
```

### Пагинация
```html
{% for page_num in range(1, total_pages + 1) %}
    {% if page_num == current_page %}
        <span class="current">{{ page_num }}</span>
    {% else %}
        <a href="{{ url_for('products', page=page_num) }}">{{ page_num }}</a>
    {% endif %}
{% endfor %}
```

### Звездный рейтинг
```html
{% set rating = 4 %}
{% for i in range(1, 6) %}
    {% if i <= rating %}
        <span class="star full">★</span>
    {% else %}
        <span class="star empty">☆</span>
    {% endif %}
{% endfor %}
```

## Полезные встроенные переменные

```html
<!-- Информация о текущем запросе -->
{{ request.method }}        <!-- GET или POST -->
{{ request.args.get('page') }}  <!-- Параметр URL -->
{{ request.form.get('name') }}  <!-- Данные формы -->

<!-- Информация о пользователе (если авторизован) -->
{{ current_user.username }}
{{ current_user.is_admin }}
```

## Лучшие практики

✅ **Делай:**
- Используй наследование шаблонов для избежания дублирования
- Группируй переиспользуемые компоненты в отдельные файлы
- Используй фильтры для форматирования данных
- Проверяй переменные перед выводом

❌ **Не делай:**
- Не пиши много логики в шаблонах
- Не используй HTML в Python-коде
- Не передавай необработанные данные из БД
- Не забывай про экранирование ({{ variable }} автоматически экранирует)

