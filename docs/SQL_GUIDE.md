# 📚 SQL Гайд для начинающих

## Что такое SQL?
SQL (Structured Query Language) — язык для работы с базами данных. Позволяет создавать, читать, обновлять и удалять данные.

## Основные команды

### 1. SELECT - Получение данных

```sql
-- Получить все данные из таблицы
SELECT * FROM products;

-- Получить конкретные колонки
SELECT name, price FROM products;

-- С условием WHERE
SELECT * FROM products WHERE price > 100;

-- С сортировкой
SELECT * FROM products ORDER BY price DESC;

-- Ограничение количества строк
SELECT * FROM products LIMIT 10;

-- С объединением условий
SELECT * FROM products WHERE price > 100 AND quantity > 0;
```

### 2. INSERT - Добавление данных

```sql
-- Добавить одну запись
INSERT INTO products (name, price, quantity) 
VALUES ('Товар', 99.99, 10);

-- Добавить несколько записей
INSERT INTO products (name, price, quantity) 
VALUES 
  ('Товар1', 50.00, 5),
  ('Товар2', 75.00, 8),
  ('Товар3', 100.00, 3);
```

### 3. UPDATE - Обновление данных

```sql
-- Изменить цену товара с ID=1
UPDATE products 
SET price = 150.00 
WHERE id = 1;

-- Изменить несколько полей
UPDATE products 
SET price = 200.00, quantity = 20 
WHERE name = 'Товар1';
```

### 4. DELETE - Удаление данных

```sql
-- Удалить товар с ID=1
DELETE FROM products 
WHERE id = 1;

-- Удалить все товары дороже 500
DELETE FROM products 
WHERE price > 500;
```

## Полезные операции

### Подсчет записей
```sql
-- Сколько товаров в таблице?
SELECT COUNT(*) FROM products;

-- Сколько товаров с ценой > 100?
SELECT COUNT(*) FROM products WHERE price > 100;
```

### Сумма и среднее значение
```sql
-- Общая стоимость всех товаров
SELECT SUM(price * quantity) FROM products;

-- Средняя цена товара
SELECT AVG(price) FROM products;

-- Минимальная и максимальная цена
SELECT MIN(price), MAX(price) FROM products;
```

### Объединение таблиц (JOIN)
```sql
-- Получить все заказы с названиями товаров
SELECT orders.id, orders.customer_name, products.name, orders.total_price
FROM orders
JOIN products ON orders.product_id = products.id;
```

### Группировка (GROUP BY)
```sql
-- Сколько заказов по каждому товару?
SELECT product_id, COUNT(*) as order_count
FROM orders
GROUP BY product_id;
```

## Примеры для нашего приложения

```sql
-- Все товары отсортированные по цене (дешевле первыми)
SELECT * FROM products ORDER BY price ASC;

-- Товары, которых нет в наличии
SELECT * FROM products WHERE quantity = 0;

-- Все заказы за последние 30 дней
SELECT * FROM orders 
WHERE created_at >= date('now', '-30 days');

-- Самый популярный товар
SELECT product_id, COUNT(*) as popularity
FROM orders
GROUP BY product_id
ORDER BY popularity DESC
LIMIT 1;

-- Общий доход
SELECT SUM(total_price) as total_revenue FROM orders;
```

## Лучшие практики

✅ **Делай:**
- Используй понятные названия таблиц и колонок
- Форматируй SQL-запросы для читаемости
- Использованиивайте WHERE для фильтрации больших данных
- Делай резервные копии перед удалением данных

❌ **Не делай:**
- Не используй SELECT * на очень больших таблицах
- Не забывай WHERE в UPDATE и DELETE
- Не передавай пользовательский ввод напрямую в запрос (используй параметры)

