"""Cau 3: Xu ly danh sach so nguyen."""


def nhap_danh_sach():
    danh_sach = []
    print("Nhap cac so nguyen (nhap 0 de ket thuc):")
    while True:
        try:
            x = int(input("Nhap x: "))
            if x == 0:
                break
            danh_sach.append(x)
        except ValueError:
            print("Du lieu khong hop le. Vui long nhap so nguyen.")
    return danh_sach


def main():
    danh_sach = nhap_danh_sach()
    print("Danh sach vua nhap:", danh_sach)

    so_duong_chan = [x for x in danh_sach if x > 0 and x % 2 == 0]
    print("Cac so duong chan:", so_duong_chan)

    try:
        k = int(input("Nhap gia tri k can dem: "))
        print(f"So lan xuat hien cua {k}: {danh_sach.count(k)}")
    except ValueError:
        print("k khong hop le. Hay nhap mot so nguyen.")


if __name__ == "__main__":
    main()
