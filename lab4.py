
DROP TABLE IF EXISTS ChiTietHD CASCADE;
DROP TABLE IF EXISTS HoaDon CASCADE;
DROP TABLE IF EXISTS SanPham CASCADE;
DROP TABLE IF EXISTS KhachHang CASCADE;
DROP TABLE IF EXISTS suppliers CASCADE;
DROP TABLE IF EXISTS test_table CASCADE;


CREATE TABLE KhachHang (
    MaKH INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    TenKH VARCHAR(255) NOT NULL,
    DienThoai VARCHAR(15) UNIQUE,
    DiaChi VARCHAR(255)
);
CREATE TABLE SanPham (
    MaSP INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    TenSP VARCHAR(255) NOT NULL,
    DonGia NUMERIC(10,2) NOT NULL CHECK (DonGia > 0)
);

CREATE TABLE HoaDon (
    MaHD INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    NgayTao DATE NOT NULL,
    MaKH INT,
    CONSTRAINT fk_khachhang
        FOREIGN KEY (MaKH) REFERENCES KhachHang(MaKH)
);

CREATE TABLE ChiTietHD (
    MaHD INT,
    MaSP INT,
    SoLuong INT NOT NULL CHECK (SoLuong > 0),
    PRIMARY KEY (MaHD, MaSP),
    CONSTRAINT fk_hd
        FOREIGN KEY (MaHD) REFERENCES HoaDon(MaHD),
    CONSTRAINT fk_sp
        FOREIGN KEY (MaSP) REFERENCES SanPham(MaSP)
);


INSERT INTO KhachHang (TenKH, DienThoai, DiaChi)
VALUES 
('Nguyen Van A', '0901234567', 'Ha Noi'),
('Tran Thi B', '0912345678', 'Hai Phong');

INSERT INTO SanPham (TenSP, DonGia)
VALUES 
('Sua tuoi', 20000),
('Mi goi', 5000),
('Nuoc suoi Aquafina', 10000);


INSERT INTO HoaDon (NgayTao, MaKH)
VALUES 
('2025-03-01', 1),
('2025-03-02', 2);


INSERT INTO ChiTietHD (MaHD, MaSP, SoLuong)
VALUES 
(1, 1, 2),
(1, 2, 3),
(2, 3, 5);

-- 3. BÀI 2: TẠO suppliers

CREATE TABLE suppliers (
    supplier_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    supplier_name VARCHAR(255) NOT NULL,
    contact_phone VARCHAR(15) UNIQUE
);

-- 4. BÀI 3: ALTER TABLE

ALTER TABLE suppliers
ADD COLUMN email VARCHAR(100);

ALTER TABLE SanPham
ADD COLUMN supplier_id INT;

ALTER TABLE SanPham
ADD CONSTRAINT fk_supplier
FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id);


-- 5. BÀI 4: INSERT / UPDATE / DELETE


INSERT INTO suppliers (supplier_name, contact_phone, email)
VALUES 
('Công ty Sữa Việt Nam', '0987654321', 'contact@vinamilk.vn'),
('Công ty Thực phẩm Á Châu', '0912345678', 'contact@acecook.vn');

UPDATE suppliers
SET contact_phone = '0911112222'
WHERE supplier_name = 'Công ty Thực phẩm Á Châu';

DELETE FROM ChiTietHD WHERE MaSP = 3;


DELETE FROM SanPham WHERE MaSP = 3;

-- 6. BÀI 5: DROP


CREATE TABLE test_table (
    id INT
);


ALTER TABLE suppliers
DROP COLUMN contact_phone;


DROP TABLE test_table;

DROP SCHEMA public CASCADE;
CREATE SCHEMA public;