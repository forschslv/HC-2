# 🎨 CSS Гайд для начинающих

## Что такое CSS?
CSS (Cascading Style Sheets) — язык для оформления веб-страниц. Определяет цвета, шрифты, размеры и расположение элементов.

## Основные селекторы

### 1. Селектор по тегу
```css
p {
    color: blue;
}
```

### 2. Селектор по классу
```css
.card {
    background-color: white;
    border-radius: 8px;
}

/* Использование в HTML -->
<div class="card">Содержимое</div>
```

### 3. Селектор по ID
```css
#header {
    background-color: navy;
    height: 100px;
}

<!-- Использование в HTML -->
<div id="header">Заголовок</div>
```

### 4. Комбинированные селекторы
```css
/* Потомок */
.container p {
    margin: 10px;
}

/* Прямой потомок */
.container > p {
    color: red;
}

/* Несколько селекторов */
h1, h2, h3 {
    font-family: Arial;
}
```

## Box Model (Модель коробки)

Каждый элемент состоит из:
```
┌─────────────────────────┐
│       margin            │
│  ┌───────────────────┐  │
│  │     border        │  │
│  │  ┌─────────────┐  │  │
│  │  │  padding    │  │  │
│  │  │ ┌─────────┐ │  │  │
│  │  │ │ content │ │  │  │
│  │  │ └─────────┘ │  │  │
│  │  └─────────────┘  │  │
│  └───────────────────┘  │
└─────────────────────────┘
```

```css
.box {
    width: 200px;
    height: 100px;
    padding: 20px;           /* Внутреннее пространство */
    margin: 15px;            /* Внешнее пространство */
    border: 2px solid black; /* Граница */
    background-color: yellow;
}
```

## Основные свойства

### Цвет и фон
```css
.element {
    color: #FF5733;              /* Цвет текста */
    background-color: #E8F4F8;   /* Цвет фона */
    background-image: url('bg.png');
}
```

### Шрифты
```css
.text {
    font-family: Arial, sans-serif;
    font-size: 18px;
    font-weight: bold;           /* 400-700 или bold, normal */
    font-style: italic;
    line-height: 1.5;            /* Высота строки */
}
```

### Размеры
```css
.container {
    width: 100%;
    max-width: 1200px;
    height: 200px;
    min-height: 100px;
}
```

### Выравнивание текста
```css
.text-center {
    text-align: center;  /* left, right, center, justify */
}

.vertical-center {
    display: flex;
    align-items: center;
    justify-content: center;
}
```

### Тени и углы
```css
.card {
    border-radius: 8px;           /* Скругленные углы */
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);  /* Тень */
    text-shadow: 2px 2px 4px grey;           /* Тень текста */
}
```

## Flexbox (Гибкая сетка)

Отличный способ выравнивания элементов:

```css
.flex-container {
    display: flex;
    justify-content: space-between;  /* space-between, center, flex-start */
    align-items: center;             /* center, flex-start, flex-end */
    gap: 20px;                       /* Промежуток между элементами */
}

.flex-item {
    flex: 1;                         /* Занять равную часть */
    min-width: 200px;
}
```

## Grid (Сетка)

Для более сложных макетов:

```css
.grid-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);  /* 3 равные колонки */
    gap: 20px;
}

.grid-item {
    background-color: lightblue;
    padding: 20px;
}
```

## Адаптивный дизайн (Media Queries)

```css
/* Для больших экранов */
.container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
}

/* Для планшетов */
@media (max-width: 768px) {
    .container {
        grid-template-columns: repeat(2, 1fr);
    }
}

/* Для мобильных */
@media (max-width: 480px) {
    .container {
        grid-template-columns: 1fr;
    }
}
```

## Переходы и анимации

### Переходы (Transitions)
```css
.button {
    background-color: blue;
    transition: background-color 0.3s ease;
}

.button:hover {
    background-color: darkblue;
}
```

### Анимации
```css
@keyframes slideIn {
    from {
        transform: translateX(-100px);
        opacity: 0;
    }
    to {
        transform: translateX(0);
        opacity: 1;
    }
}

.animated {
    animation: slideIn 0.5s ease-in-out;
}
```

## Примеры для нашего приложения

### Карточка товара
```css
.product-card {
    background-color: white;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    transition: transform 0.3s, box-shadow 0.3s;
}

.product-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0,0,0,0.15);
}
```

### Таблица
```css
.table {
    width: 100%;
    border-collapse: collapse;
}

.table th {
    background-color: #333;
    color: white;
    padding: 12px;
    text-align: left;
}

.table td {
    padding: 12px;
    border-bottom: 1px solid #ddd;
}

.table tr:hover {
    background-color: #f5f5f5;
}
```

### Навигация
```css
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #333;
    color: white;
    padding: 15px 30px;
}

.navbar a {
    color: white;
    text-decoration: none;
    margin: 0 15px;
    transition: color 0.3s;
}

.navbar a:hover {
    color: #4CAF50;
}
```

## Полезные советы

✅ **Делай:**
- Используй классы вместо ID для стилей
- Организуй CSS по разделам (навигация, карточки, формы)
- Используй переменные CSS (custom properties)
- Тестируй на мобильных устройствах

❌ **Не делай:**
- Не используй слишком специфичные селекторы
- Не зависай в !important
- Не забывай про адаптивный дизайн
- Не копируй целые стили, используй классы

## Переменные CSS

```css
:root {
    --primary-color: #0d6efd;
    --secondary-color: #6c757d;
    --border-radius: 8px;
    --box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.button {
    background-color: var(--primary-color);
    border-radius: var(--border-radius);
    box-shadow: var(--box-shadow);
}
```

## Bootstrap классы (уже подключены в проекте)

```html
<!-- Контейнер -->
<div class="container">
    <!-- Сетка: 12 колонок -->
    <div class="row">
        <div class="col-md-6">На 50% экрана</div>
        <div class="col-md-6">На 50% экрана</div>
    </div>
</div>

<!-- Кнопки -->
<button class="btn btn-primary">Первичная</button>
<button class="btn btn-success">Успех</button>
<button class="btn btn-danger">Опасность</button>

<!-- Карточки -->
<div class="card">
    <div class="card-header">Заголовок</div>
    <div class="card-body">Содержимое</div>
</div>

<!-- Таблицы -->
<table class="table table-striped">
    <tr><th>Колонка 1</th><th>Колонка 2</th></tr>
</table>
```

