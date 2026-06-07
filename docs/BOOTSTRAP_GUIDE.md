# 🎨 Bootstrap 5 Полный Гайд

## Подключение Bootstrap

```html
<!-- CSS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

<!-- JavaScript -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
```

## Grid система (12 колонок)

```html
<div class="container">
    <div class="row">
        <div class="col-md-4">33%</div>
        <div class="col-md-4">33%</div>
        <div class="col-md-4">33%</div>
    </div>
</div>
```

## Точки останова (Breakpoints)

```
col      - все экраны
col-sm   - маленькие (576px+)
col-md   - средние (768px+)
col-lg   - большие (992px+)
col-xl   - очень большие (1200px+)
```

## Кнопки

```html
<button class="btn btn-primary">Primary</button>
<button class="btn btn-success">Success</button>
<button class="btn btn-danger">Danger</button>
<button class="btn btn-lg">Большая</button>
<button class="btn btn-sm">Маленькая</button>
```

## Карточки

```html
<div class="card">
    <div class="card-body">
        <h5 class="card-title">Заголовок</h5>
        <p class="card-text">Содержимое</p>
        <a href="#" class="btn btn-primary">Кнопка</a>
    </div>
</div>
```

## Таблицы

```html
<table class="table table-striped table-hover">
    <thead class="table-dark">
        <tr><th>Столбец 1</th><th>Столбец 2</th></tr>
    </thead>
    <tbody>
        <tr><td>Данные 1</td><td>Данные 2</td></tr>
    </tbody>
</table>
```

## Формы

```html
<form>
    <div class="mb-3">
        <label for="name" class="form-label">Имя</label>
        <input type="text" class="form-control" id="name">
    </div>
    <button type="submit" class="btn btn-primary">Отправить</button>
</form>
```

## Модальные окна

```html
<button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#myModal">
    Открыть
</button>

<div class="modal fade" id="myModal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Заголовок</h5>
            </div>
            <div class="modal-body">Содержимое</div>
        </div>
    </div>
</div>
```

## Алерты

```html
<div class="alert alert-success">Успешно!</div>
<div class="alert alert-danger">Ошибка!</div>
<div class="alert alert-warning alert-dismissible fade show">
    Предупреждение
    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
</div>
```

## Утилиты

```html
<!-- Отступы -->
<div class="m-3">Margin 3</div>
<div class="p-3">Padding 3</div>

<!-- Текст -->
<p class="text-center">Центр</p>
<p class="text-danger">Красный</p>
<p class="fw-bold">Жирный</p>

<!-- Flexbox -->
<div class="d-flex justify-content-between">
    <div>Слева</div>
    <div>Справа</div>
</div>
```

## Navbar

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
        <a class="navbar-brand" href="/">Сайт</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item"><a class="nav-link" href="/">Главная</a></li>
                <li class="nav-item"><a class="nav-link" href="/products">Товары</a></li>
            </ul>
        </div>
    </div>
</nav>
```

