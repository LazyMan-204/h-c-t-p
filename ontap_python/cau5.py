"""Cau 5: Tao lop DienThoai va khoi tao hai doi tuong."""


class DienThoai:
    def __init__(self, ma_may, ten_may, hang_san_xuat, dung_luong_pin, gia_ban):
        self.MaMay = ma_may
        self.TenMay = ten_may
        self.HangSanXuat = hang_san_xuat
        self.DungLuongPin = dung_luong_pin
        self.GiaBan = gia_ban

    def thongtindienthoai(self):
        print("Ma may:", self.MaMay)
        print("Ten may:", self.TenMay)
        print("Hang san xuat:", self.HangSanXuat)
        print("Dung luong pin:", self.DungLuongPin, "mAh")
        print("Gia ban:", f"{self.GiaBan:,}", "VND")


def main():
    dt01 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
    dt02 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 27990000)

    print("=== DIEN THOAI 1 ===")
    dt01.thongtindienthoai()

    print("\n=== DIEN THOAI 2 ===")
    dt02.thongtindienthoai()


if __name__ == "__main__":
    main()
