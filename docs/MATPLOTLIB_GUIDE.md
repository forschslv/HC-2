# 📈 Matplotlib Гайд для графиков

## Установка

```bash
pip install matplotlib
```

## Базовый график

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 24, 36, 18, 7]

plt.plot(x, y)
plt.xlabel('X ось')
plt.ylabel('Y ось')
plt.title('Простой график')
plt.show()
```

## Типы графиков

### Столбчатая диаграмма
```python
import matplotlib.pyplot as plt

products = ['Ноутбук', 'Мышь', 'Клавиатура']
prices = [50000, 1500, 3000]

plt.bar(products, prices, color='skyblue')
plt.title('Цены товаров')
plt.ylabel('Цена (₽)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

### Круговая диаграмма
```python
import matplotlib.pyplot as plt

categories = ['Электроника', 'Одежда', 'Книги']
sizes = [40, 25, 35]

plt.pie(sizes, labels=categories, autopct='%1.1f%%')
plt.title('Распределение')
plt.show()
```

### График линий
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y, marker='o', linestyle='-', linewidth=2)
plt.title('График')
plt.grid(True, alpha=0.3)
plt.show()
```

## Использование в Flask

```python
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Важно для сервера!

import os

@app.route('/statistics')
def statistics():
    products = Product.query.all()
    names = [p.name for p in products]
    prices = [p.price for p in products]
    
    plt.figure(figsize=(10, 6))
    plt.bar(names, prices, color='skyblue')
    plt.title('Цены товаров')
    plt.xticks(rotation=45)
    
    os.makedirs('static/charts', exist_ok=True)
    plt.savefig('static/charts/prices.png', dpi=100, bbox_inches='tight')
    plt.close()
    
    return render_template('statistics.html')
```

## Несколько графиков

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0, 0].plot([1, 2, 3], [10, 20, 15])
axes[0, 0].set_title('График 1')

axes[0, 1].bar(['A', 'B', 'C'], [10, 20, 15])
axes[0, 1].set_title('График 2')

axes[1, 0].pie([30, 20, 50], labels=['X', 'Y', 'Z'])
axes[1, 0].set_title('График 3')

axes[1, 1].scatter([1, 2, 3], [10, 20, 15])
axes[1, 1].set_title('График 4')

plt.tight_layout()
plt.savefig('charts.png')
plt.close()
```

## Сохранение графика

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [10, 20, 15])
plt.title('Мой график')

# PNG
plt.savefig('graph.png', dpi=300, bbox_inches='tight')

# PDF
plt.savefig('graph.pdf', bbox_inches='tight')

# SVG
plt.savefig('graph.svg', bbox_inches='tight')

plt.show()
```

## Стилизация

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 15, 25, 30]
y2 = [5, 15, 20, 10, 25]

plt.plot(x, y1, color='red', linestyle='--', label='Ряд 1')
plt.plot(x, y2, color='blue', linestyle='-', label='Ряд 2')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('График со стилем')
plt.legend()
plt.grid(True)
plt.show()
```

## Важные советы

✅ Используй `matplotlib.use('Agg')` в Flask  
✅ Всегда закрывай графики: `plt.close()`  
✅ Используй `os.makedirs()` для папок  
✅ Сохраняй с хорошим разрешением (dpi=300)  
✅ Используй `tight_layout()` для лучшего расположения  
✅ Не используй `plt.show()` на сервере

