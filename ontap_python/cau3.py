"""Cau 3: Nhap danh sach den khi gap 0, tinh tong va dem tan suat."""


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
            print("Vui long nhap so nguyen.")
    return danh_sach


def tong_so_chan_duong(danh_sach):
    return sum(x for x in danh_sach if x > 0 and x % 2 == 0)


def dem_so_lan_xuat_hien(danh_sach, k):
    return danh_sach.count(k)


def main():
    danh_sach = nhap_danh_sach()
    print("Danh sach vua nhap:", danh_sach)
    print("Tong cac so chan duong:", tong_so_chan_duong(danh_sach))

    try:
        k = int(input("Nhap gia tri k can dem: "))
        print(f"So lan {k} xuat hien:", dem_so_lan_xuat_hien(danh_sach, k))
    except ValueError:
        print("k phai la mot so nguyen.")


if __name__ == "__main__":
    main()
