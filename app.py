"""
Главное приложение Flask для хакатона
Демонстрирует основные возможности: маршруты, работу с БД, формы, JSON, CSV, графики
"""

from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Используем backend без GUI

# Инициализация приложения
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_database.db'
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Инициализация БД
db = SQLAlchemy(app)

# ==================== МОДЕЛИ БД ====================
class Product(db.Model):
    """Модель для товаров"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'quantity': self.quantity,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }


class Order(db.Model):
    """Модель для заказов"""
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    total_price = db.Column(db.Float)
    status = db.Column(db.String(50), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    product = db.relationship('Product', backref='orders')

    def to_dict(self):
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'product_name': self.product.name,
            'quantity': self.quantity,
            'total_price': self.total_price,
            'status': self.status,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }


# ==================== КОНТЕКСТ ПРИЛОЖЕНИЯ ====================
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Product': Product, 'Order': Order}


# ==================== МАРШРУТЫ ====================

@app.route('/')
def index():
    """Главная страница"""
    products_count = Product.query.count()
    orders_count = Order.query.count()
    
    context = {
        'page_title': 'Главная',
        'products_count': products_count,
        'orders_count': orders_count,
        'total_revenue': db.session.query(db.func.sum(Order.total_price)).scalar() or 0
    }
    return render_template('index.html', **context)


@app.route('/products', methods=['GET', 'POST'])
def products():
    """Страница с товарами"""
    if request.method == 'POST':
        # Обработка добавления нового товара
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        quantity = request.form.get('quantity')
        
        if name and price:
            new_product = Product(
                name=name,
                description=description,
                price=float(price),
                quantity=int(quantity) if quantity else 0
            )
            db.session.add(new_product)
            db.session.commit()
            return redirect(url_for('products'))
    
    products_list = Product.query.all()
    context = {
        'page_title': 'Товары',
        'products': products_list,
        'total_products': len(products_list)
    }
    return render_template('products.html', **context)


@app.route('/product/<int:product_id>')
def product_detail(product_id):
    """Страница с деталями товара"""
    product = Product.query.get_or_404(product_id)
    orders = Order.query.filter_by(product_id=product_id).all()
    
    context = {
        'page_title': f'Товар: {product.name}',
        'product': product,
        'orders_count': len(orders),
        'related_products': Product.query.filter(Product.id != product_id).limit(3).all()
    }
    return render_template('product_detail.html', **context)


@app.route('/orders', methods=['GET', 'POST'])
def orders():
    """Страница с заказами"""
    if request.method == 'POST':
        # Обработка создания нового заказа
        customer_name = request.form.get('customer_name')
        product_id = request.form.get('product_id')
        quantity = request.form.get('quantity')
        
        product = Product.query.get(product_id)
        if product and customer_name and quantity:
            total_price = product.price * int(quantity)
            new_order = Order(
                customer_name=customer_name,
                product_id=int(product_id),
                quantity=int(quantity),
                total_price=total_price
            )
            db.session.add(new_order)
            db.session.commit()
            return redirect(url_for('orders'))
    
    orders_list = Order.query.all()
    products_list = Product.query.all()
    
    context = {
        'page_title': 'Заказы',
        'orders': orders_list,
        'products': products_list,
        'total_orders': len(orders_list)
    }
    return render_template('orders.html', **context)


@app.route('/statistics')
def statistics():
    """Страница со статистикой"""
    products = Product.query.all()
    
    # Подготовка данных для графиков
    product_names = [p.name for p in products]
    product_prices = [p.price for p in products]
    product_quantities = [p.quantity for p in products]
    
    # Создание графиков
    generate_charts(product_names, product_prices, product_quantities)
    
    context = {
        'page_title': 'Статистика',
        'total_products': len(products),
        'total_orders': Order.query.count(),
        'avg_price': sum(p.price for p in products) / len(products) if products else 0,
        'total_revenue': db.session.query(db.func.sum(Order.total_price)).scalar() or 0
    }
    return render_template('statistics.html', **context)


@app.route('/api/products', methods=['GET'])
def api_products():
    """API для получения товаров в JSON"""
    products_list = Product.query.all()
    return jsonify([p.to_dict() for p in products_list])


@app.route('/api/orders', methods=['GET'])
def api_orders():
    """API для получения заказов в JSON"""
    orders_list = Order.query.all()
    return jsonify([o.to_dict() for o in orders_list])


@app.route('/export/products')
def export_products_csv():
    """Экспорт товаров в CSV"""
    products_list = Product.query.all()
    
    csv_path = 'exports/products.csv'
    os.makedirs('exports', exist_ok=True)
    
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Название', 'Описание', 'Цена', 'Количество', 'Дата создания'])
        
        for product in products_list:
            writer.writerow([
                product.id,
                product.name,
                product.description,
                product.price,
                product.quantity,
                product.created_at.strftime('%Y-%m-%d %H:%M:%S')
            ])
    
    return redirect(url_for('index'))


# ==================== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ====================

def generate_charts(names, prices, quantities):
    """Генерирует графики для статистики"""
    plt.figure(figsize=(12, 8))
    
    # График 1: Цены
    plt.subplot(2, 2, 1)
    plt.bar(names, prices, color='skyblue')
    plt.title('Цены товаров')
    plt.xticks(rotation=45)
    
    # График 2: Количество
    plt.subplot(2, 2, 2)
    plt.bar(names, quantities, color='lightcoral')
    plt.title('Количество товаров на складе')
    plt.xticks(rotation=45)
    
    # График 3: Круговая диаграмма
    plt.subplot(2, 2, 3)
    if quantities and sum(quantities) > 0:
        plt.pie(quantities, labels=names, autopct='%1.1f%%')
        plt.title('Распределение товаров')
    
    plt.tight_layout()
    os.makedirs('static/charts', exist_ok=True)
    plt.savefig('static/charts/statistics.png')
    plt.close()


# ==================== ОБРАБОТКА ОШИБОК ====================

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', error_code=404, error_message='Страница не найдена'), 404


@app.errorhandler(500)
def server_error(error):
    return render_template('error.html', error_code=500, error_message='Ошибка сервера'), 500


# ==================== ИНИЦИАЛИЗАЦИЯ ====================

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='localhost', port=5000)

