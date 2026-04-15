-- Y4: 10 đơn hàng gần nhất
SELECT 
    o.order_id,
    c.name AS customer_name,
    e.name AS employee_name,
    o.order_date,
    SUM(oi.quantity * oi.price) AS total_amount
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN employees e ON o.employee_id = e.employee_id
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY o.order_id, c.name, e.name, o.order_date
ORDER BY o.order_date DESC
LIMIT 10;


-- Y5: Doanh thu theo danh mục (>1,000,000)
SELECT 
    pc.category_name,
    SUM(oi.quantity * oi.price) AS revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
JOIN product_categories pc ON p.category_id = pc.category_id
GROUP BY pc.category_name
HAVING SUM(oi.quantity * oi.price) > 1000000
ORDER BY revenue DESC;


-- Y6: Subquery tìm sản phẩm theo nhà cung cấp
SELECT product_name, price
FROM products
WHERE supplier_id = (
    SELECT supplier_id
    FROM suppliers
    WHERE supplier_name = 'Công ty Thực phẩm Hảo Hạng'
);


-- Y7: Xếp hạng nhân viên tháng 10/2025
SELECT 
    e.name,
    SUM(oi.quantity * oi.price) AS total_revenue,
    DENSE_RANK() OVER (
        ORDER BY SUM(oi.quantity * oi.price) DESC
    ) AS rank
FROM orders o
JOIN employees e ON o.employee_id = e.employee_id
JOIN order_items oi ON o.order_id = oi.order_id
WHERE EXTRACT(MONTH FROM o.order_date) = 10
  AND EXTRACT(YEAR FROM o.order_date) = 2025
GROUP BY e.name;


-- Y8: Phân tích hiệu năng (chưa có index)

-- 1. Thêm 50,000 khách hàng
INSERT INTO customers (name, email, phone, address)
SELECT 
    'User ' || i,
    'user' || i || '@gmail.com',
    '0909999' || i,
    'Hà Nội'
FROM generate_series(1,50000) i;

-- 2. EXPLAIN ANALYZE (trước index)
EXPLAIN ANALYZE
SELECT *
FROM customers
WHERE email = 'user100@gmail.com';


-- Y9: Tạo index + chạy lại EXPLAIN

-- 1. Tạo index
CREATE INDEX idx_customers_email
ON customers(email);

-- 2. Chạy lại EXPLAIN ANALYZE
EXPLAIN ANALYZE
SELECT *
FROM customers
WHERE email = 'user100@gmail.com';

