-- 1. Xóa và tạo database
DROP DATABASE IF EXISTS lab3;
CREATE DATABASE lab3;;

-- 2. Xóa bảng
DROP TABLE IF EXISTS order_details CASCADE;
DROP TABLE IF EXISTS orders CASCADE;
DROP TABLE IF EXISTS products CASCADE;
DROP TABLE IF EXISTS customers CASCADE;
DROP TABLE IF EXISTS suppliers CASCADE;


-- 3. Bảng customers
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    address VARCHAR(200)
);

-- 4. Bảng products
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(15,2)
);

-- 5. Bảng orders
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id) ON DELETE CASCADE,
    order_date TIMESTAMP DEFAULT NOW(),
    total_amount DECIMAL(15,2) DEFAULT 0
);

-- 6. Bảng order_details
CREATE TABLE order_details (
    order_id INT REFERENCES orders(order_id) ON DELETE CASCADE,
    product_id INT REFERENCES products(product_id),
    quantity INT CHECK (quantity > 0),
    unit_price DECIMAL(15,2),
    PRIMARY KEY (order_id, product_id)
);
INSERT INTO customers (full_name, phone, address) VALUES
('Nguyễn Văn An', '0901234567', '123 Lê Lợi, TP.HCM'),
('Trần Thị Bình', '0912345678', '456 Nguyễn Huệ, Hà Nội'),
('Lê Văn Cường', '0987654321', '789 Trần Hưng Đạo, Đà Nẵng'),
('Phạm Minh Đức', '0933445566', '101 Hai Bà Trưng, Cần Thơ'),
('Nguyễn Văn Em', '0944556677', '202 Lý Tự Trọng, Hải Phòng');

INSERT INTO products (product_name, price) VALUES
('Laptop Dell XPS', 25000000),
('iPhone 15 Pro', 28000000),
('Chuột Logitech G502', 1200000),
('Bàn phím cơ Akko', 1500000),
('Màn hình LG 27 inch', 5500000);

INSERT INTO orders (customer_id, order_date, total_amount) VALUES
(1, '2023-10-01 10:00:00', 26200000),
(2, '2023-10-02 11:30:00', 28000000),
(3, '2023-10-03 09:15:00', 1200000),
(1, '2023-10-04 14:45:00', 1500000),
(5, '2023-10-05 16:20:00', 5500000);

INSERT INTO order_details (order_id, product_id, quantity, unit_price) VALUES
(1, 1, 1, 25000000),
(1, 3, 1, 1200000),  
(2, 2, 1, 28000000), 
(3, 3, 1, 1200000),  
(4, 4, 1, 1500000),  
(5, 5, 1, 5500000); 

--lab5

-- Tạo bảng suppliers để làm bài 2, 3, 4
CREATE TABLE suppliers (
    supplier_id SERIAL PRIMARY KEY,
    supplier_name VARCHAR(100) NOT NULL,
    contact_phone VARCHAR(20)
);

-- Thêm cột supplier_id vào bảng products [cite: 18]
ALTER TABLE products 
ADD COLUMN supplier_id INT 
REFERENCES suppliers(supplier_id);

-- Thêm dữ liệu mẫu cho nhà cung cấp
INSERT INTO suppliers (supplier_name, contact_phone) VALUES
(N'Công ty Sữa Việt Nam', '02812345678'),
(N'Điện tử Samsung', '02888888888');

-- Cập nhật supplier_id cho các sản phẩm đã có [cite: 18]
UPDATE products SET supplier_id = 1 WHERE product_id IN (1, 2);
UPDATE products SET supplier_id = 2 WHERE product_id IN (3, 4, 5);


-- BÀI 1: JOIN CƠ BẢN [cite: 22]

-- 1. (INNER JOIN) Hiển thị chi tiết các sản phẩm đã được bán 
-- Kết quả: order_id, product_name, quantity, price 
SELECT 
    od.order_id, 
    p.product_name, 
    od.quantity, 
    od.unit_price AS price
FROM products p
INNER JOIN order_details od ON p.product_id = od.product_id;

-- 2. (LEFT JOIN) Liệt kê tất cả khách hàng và đơn hàng (kể cả chưa mua)

SELECT
    c.full_name, 
    o.order_id
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;


-- BÀI 2: JOIN NÂNG CAO & UNION 

-- 1. (RIGHT JOIN) Liệt kê tất cả sản phẩm và đơn hàng tương ứng 
SELECT 
    p.product_name, 
    od.order_id
FROM order_details od
RIGHT JOIN products p ON od.product_id = p.product_id;

-- 2. (UNION) Tạo danh bạ liên hệ duy nhất từ khách hàng và nhà cung cấp 
-- Không được có dòng trùng lặp 
SELECT full_name AS ContactName, phone AS PhoneNumber FROM customers
UNION
SELECT supplier_name AS ContactName, contact_phone AS PhoneNumber FROM suppliers;


-- BÀI 3: SUBQUERY TRONG WHERE VÀ SELECT 

-- 1. (Subquery với IN) Tìm sản phẩm cung cấp bởi 'Công ty Sữa Việt Nam' 
SELECT product_name, price
FROM products
WHERE supplier_id IN (
    SELECT supplier_id 
    FROM suppliers 
    WHERE supplier_name = N'Công ty Sữa Việt Nam'
);

-- 2. (Subquery trong SELECT) Hiển thị giá sản phẩm và giá trung bình
SELECT 
    product_name, 
    price, 
    (SELECT AVG(price) FROM products) AS average_price
FROM products;


-- BÀI 4: SUBQUERY VỚI FROM VÀ EXISTS 

-- 1. (Subquery trong FROM) Tìm đơn hàng có tổng giá trị > 50,000đ 
SELECT order_id, total_value
FROM (
    SELECT order_id, SUM(quantity * unit_price) AS total_value
    FROM order_details
    GROUP BY order_id
) AS temp_table
WHERE total_value > 50000;
S
-- 2. (EXISTS) Liệt kê các nhà cung cấp có ít nhất một sản phẩm 
SELECT supplier_name
FROM suppliers s
WHERE EXISTS (
    SELECT 1 
    FROM products p 
    WHERE p.supplier_id = s.supplier_id
);
