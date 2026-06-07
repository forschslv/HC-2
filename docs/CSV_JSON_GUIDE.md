# 📦 CSV и JSON Гайд

## CSV (Comma-Separated Values)

CSV — простой текстовый формат для хранения табличных данных.

### Чтение CSV

```python
import csv

# Способ 1: DictReader
with open('products.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']}: {row['price']} ₽")

# Способ 2: reader
with open('products.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # Пропустить заголовок
    for row in reader:
        print(f"{row[0]}: {row[1]}")
```

### Запись CSV

```python
import csv

data = [
    {'id': 1, 'name': 'Товар1', 'price': 100},
    {'id': 2, 'name': 'Товар2', 'price': 200}
]

with open('products.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['id', 'name', 'price'])
    writer.writeheader()
    writer.writerows(data)
```

### Экспорт из БД в CSV

```python
import csv
from app import Product

@app.route('/export/csv')
def export_csv():
    products = Product.query.all()
    
    with open('products.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Название', 'Цена'])
        
        for product in products:
            writer.writerow([product.id, product.name, product.price])
    
    return redirect(url_for('index'))
```

## JSON (JavaScript Object Notation)

JSON — универсальный формат для обмена данными.

### Чтение JSON

```python
import json

with open('products.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for product in data['products']:
        print(f"{product['name']}: {product['price']} ₽")

# Или из строки
json_string = '{"name": "Товар", "price": 100}'
data = json.loads(json_string)
print(data['name'])
```

### Запись JSON

```python
import json

data = {
    'products': [
        {'id': 1, 'name': 'Товар1', 'price': 100},
        {'id': 2, 'name': 'Товар2', 'price': 200}
    ]
}

# В файл
with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Или в строку
json_string = json.dumps(data, ensure_ascii=False, indent=2)
```

## Flask JSON API

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

@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.get_json()
    product = Product(name=data['name'], price=data['price'])
    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'Создано', 'id': product.id}), 201
```

## Конвертирование

### CSV → JSON
```python
import csv
import json

with open('products.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    products = list(reader)

with open('products.json', 'w', encoding='utf-8') as f:
    json.dump({'products': products}, f, ensure_ascii=False, indent=2)
```

### JSON → CSV
```python
import json
import csv

with open('products.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    products = data['products']

with open('products.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=products[0].keys())
    writer.writeheader()
    writer.writerows(products)
```

## Лучшие практики

✅ Используй UTF-8 кодировку  
✅ Добавляй заголовки в CSV  
✅ Форматируй JSON с indent=2  
✅ Используй ensure_ascii=False для русского текста  
✅ Обработай ошибки при чтении файлов

