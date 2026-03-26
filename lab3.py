CREATE TABLE khach_hang (
    ma_khach_hang INT PRIMARY KEY,
    ho_ten VARCHAR(255),
    so_dien_thoai VARCHAR(15),
    dia_chi VARCHAR(255)
);

CREATE TABLE san_pham (
    ma_san_pham INT PRIMARY KEY,
    ten_san_pham VARCHAR(255),
    gia_tien DECIMAL(10,2)
);


INSERT INTO khach_hang VALUES
(1, 'Nguyen Van Anh', '0123456789', 'Ha Noi'),
(2, 'Tran Van Bach', '0987654321', 'Hai Phong'),
(3, 'Le Thi Chi', '0111222333', 'Da Nang'),
(4, 'Pham Van Dung', '0222333444', 'Ha Noi'),
(5, 'Hoang Van Em', '0333444555', 'HCM'),
(6, 'Do Thi Thao', '0444555666', 'Hue'),
(7, 'Bui Van Giang', '0555666777', 'Nam Dinh'),
(8, 'Dang Van Hieu', '0666777888', 'Hai Duong'),
(9, 'Nguyen Thi Van', '0777888999', 'Can Tho'),
(10, 'Vu Van Khanh', '0888999000', 'Ha Noi');

INSERT INTO san_pham VALUES
(1, 'Banh mi', 10000),
(2, 'Sua tuoi', 15000),
(3, 'Mi goi', 5000),
(4, 'Nuoc ngot', 12000),
(5, 'Tra sua', 30000),
(6, 'Ca phe', 25000),
(7, 'Banh ngot', 20000),
(8, 'Keo', 8000),
(9, 'Snack', 10000),
(10, 'Nuoc suoi', 7000),
(11, 'Sua chua', 6000),
(12, 'Trung ga', 3000),
(13, 'Com hop', 35000),
(14, 'Xuc xich', 15000),
(15, 'Pho goi', 7000),
(16, 'Bun tuoi', 10000),
(17, 'Rau sach', 12000),
(18, 'Thit heo', 90000),
(19, 'Ca tuoi', 80000),
(20, 'Tom', 100000);


SELECT ten_san_pham AS TenSanPham,
       gia_tien AS DonGia
FROM san_pham;

SELECT ho_ten, so_dien_thoai
FROM khach_hang
WHERE ho_ten LIKE '%Van%';

SELECT ten_san_pham, gia_tien
FROM san_pham
ORDER BY gia_tien DESC;

SELECT ten_san_pham, gia_tien
FROM san_pham
ORDER BY gia_tien ASC
LIMIT 3;