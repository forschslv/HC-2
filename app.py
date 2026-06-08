"""
Главное приложение Flask для хакатона
Демонстрирует основные возможности: маршруты, работу с БД, формы, JSON, CSV, графики
"""

from flask import Flask, render_template, request, redirect, url_for, jsonify, session, flash, abort, g
from flask_sqlalchemy import SQLAlchemy
import json
import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
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

# Новая модель User с ролью
class User(db.Model):
    """Модель для пользователей с ролями: buyer, seller, admin"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='buyer')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'role': self.role,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

# ==================== АУТЕНТИФИКАЦИЯ / РОЛИ ====================
# Контекст: доступны current_user и current_role в шаблонах
@app.context_processor
def inject_user():
    user = None
    role = None
    username = None
    if 'user_id' in session:
        user = User.query.get(session.get('user_id'))
        if user:
            role = user.role
            username = user.username
    return {'current_user': user, 'current_role': role, 'current_username': username}

# before_request для установки g.user (опционально)
@app.before_request
def load_user():
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session.get('user_id'))

# Декоратор для проверки ролей
def role_required(allowed_roles):
    if isinstance(allowed_roles, str):
        allowed = [allowed_roles]
    else:
        allowed = list(allowed_roles)
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if 'user_id' not in session:
                flash('Требуется авторизация', 'warning')
                return redirect(url_for('login'))
            user = User.query.get(session.get('user_id'))
            if not user or user.role not in allowed:
                abort(403)
            return f(*args, **kwargs)
        return wrapped
    return decorator

# ==================== КОНТЕКСТ ПРИЛОЖЕНИЯ ====================
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Product': Product, 'Order': Order, 'User': User}


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
        # Проверка прав: только продавец или админ могут добавлять товары
        if 'user_id' not in session:
            flash('Требуется вход для добавления товара', 'warning')
            return redirect(url_for('login'))
        current = User.query.get(session.get('user_id'))
        if not current or current.role not in ['seller', 'admin']:
            abort(403)

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
            flash('Товар успешно добавлен', 'success')
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
        # Разрешено создавать заказ покупателям и админам
        if 'user_id' not in session:
            flash('Требуется вход для создания заказа', 'warning')
            return redirect(url_for('login'))
        current = User.query.get(session.get('user_id'))
        if not current or current.role not in ['buyer', 'admin']:
            abort(403)

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
            flash('Заказ создан', 'success')
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


# ==================== АУТЕНТИФИКАЦИЯ: register / login / logout ====================


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Маршрут для регистрации пользователей"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        role = request.form.get('role') or 'buyer'

        if not username or not password:
            flash('Введите имя пользователя и пароль', 'warning')
            return redirect(url_for('register'))

        # Проверка назначения роли admin: если уже есть админ, то только текущий админ может назначать
        existing_admin = User.query.filter_by(role='admin').first()
        if role == 'admin' and existing_admin:
            if 'user_id' not in session:
                flash('Только администратор может создавать аккаунт с ролью admin', 'warning')
                return redirect(url_for('login'))
            current = User.query.get(session.get('user_id'))
            if not current or current.role != 'admin':
                abort(403)

        if User.query.filter_by(username=username).first():
            flash('Пользователь с таким именем уже существует', 'warning')
            return redirect(url_for('register'))

        user = User(username=username, role=role)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Регистрация успешна. Пожалуйста, войдите.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', page_title='Регистрация')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Маршрут для входа пользователей"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            flash('Неверное имя пользователя или пароль', 'danger')
            return redirect(url_for('login'))
        session['user_id'] = user.id
        flash(f'Добро пожаловать, {user.username}!', 'success')
        return redirect(url_for('index'))
    return render_template('login.html', page_title='Вход')


@app.route('/logout')
def logout():
    """Маршрут для выхода пользователей"""
    session.pop('user_id', None)
    flash('Вы вышли из системы', 'info')
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


# Обработчик 403
@app.errorhandler(403)
def forbidden(error):
    return render_template('error.html', error_code=403, error_message='Доступ запрещён'), 403


# ==================== ИНИЦИАЛИЗАЦИЯ ====================

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='localhost', port=5000)

