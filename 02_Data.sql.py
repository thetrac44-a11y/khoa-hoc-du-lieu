-- Thêm vào đầu file 02_Data.sql
TRUNCATE TABLE order_items, orders, products, customers, employees, promotions, product_categories, suppliers RESTART IDENTITY;
-- =========================
-- 1. product_categories (5)
-- =========================
INSERT INTO product_categories (category_name) VALUES
('Đồ uống'),
('Thực phẩm'),
('Bánh kẹo'),
('Gia dụng'),
('Rau củ');

-- =========================
-- 2. suppliers (5)
-- =========================
INSERT INTO suppliers (supplier_name, contact_info) VALUES
('Công ty Vinamilk', 'vinamilk@gmail.com'),
('Công ty Masan', 'masan@gmail.com'),
('Công ty Kinh Đô', 'kinhdo@gmail.com'),
('Công ty Unilever', 'unilever@gmail.com'),
('Công ty Thực phẩm Hảo Hạng', 'haohang@gmail.com');

-- =========================
-- 3. promotions (3)
-- =========================
INSERT INTO promotions (name, discount_percent, start_date, end_date) VALUES
('Khuyến mãi Tết', 10, '2025-01-01', '2025-01-31'),
('Sale mùa hè', 15, '2025-06-01', '2025-06-30'),
('Black Friday', 20, '2025-11-01', '2025-11-30');

-- =========================
-- 4. employees (10)
-- =========================
INSERT INTO employees (name, position, hire_date) VALUES
('Nguyễn Văn A', 'Thu ngân', '2023-01-01'),
('Trần Văn B', 'Thu ngân', '2023-02-01'),
('Lê Văn C', 'Quản lý', '2022-05-01'),
('Phạm Văn D', 'Kho', '2023-03-01'),
('Hoàng Văn E', 'Thu ngân', '2023-04-01'),
('Nguyễn Văn F', 'Kho', '2023-05-01'),
('Trần Văn G', 'Thu ngân', '2023-06-01'),
('Lê Văn H', 'Quản lý', '2022-07-01'),
('Phạm Văn I', 'Thu ngân', '2023-08-01'),
('Hoàng Văn K', 'Kho', '2023-09-01');

-- =========================
-- 5. customers (50)
-- =========================
INSERT INTO customers (name, email, phone, address)
SELECT 
    'Khách hàng ' || i,
    'customer' || i || '@gmail.com',
    '0900000' || i,
    'Hà Nội'
FROM generate_series(1,50) i;

-- =========================
-- 6. products (30)
-- =========================
INSERT INTO products (product_name, price, category_id, supplier_id)
SELECT 
    'Sản phẩm ' || i,
    (RANDOM()*100000 + 10000)::NUMERIC(10,2),
    (i % 5) + 1,
    (i % 5) + 1
FROM generate_series(1,30) i;

-- =========================
-- 7. orders (100)
-- =========================
INSERT INTO orders (customer_id, employee_id, promotion_id, order_date)
SELECT 
    (RANDOM()*49 + 1)::INT,
    (RANDOM()*9 + 1)::INT,
    (RANDOM()*2 + 1)::INT,
    DATE '2025-10-01' + (RANDOM()*30)::INT
FROM generate_series(1,100);

-- =========================
-- 8. order_items (>=100)
-- =========================
INSERT INTO order_items (order_id, product_id, quantity, price)
SELECT 
    (RANDOM()*99 + 1)::INT,
    (RANDOM()*29 + 1)::INT,
    (RANDOM()*5 + 1)::INT,
    (RANDOM()*100000 + 10000)::NUMERIC(10,2)
FROM generate_series(1,200);