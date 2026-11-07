"""Cau 1: Kiem tra n, dem chu so le va tinh tong S."""


def nhap_n():
    while True:
        try:
            n = int(input("Nhap so nguyen duong n (1..1500): "))
            if 1 <= n <= 1500:
                return n
            print("n phai nam trong doan [1, 1500]. Vui long nhap lai.")
        except ValueError:
            print("Du lieu khong hop le. Hay nhap mot so nguyen.")


def dem_chu_so_le(n):
    dem = 0
    for chu_so in str(n):
        if int(chu_so) % 2 != 0:
            dem += 1
    return dem


def tinh_tong(n):
    # S = 1/2 + 1/4 + 1/6 + ... + 1/(2*n)
    return sum(1 / (2 * i) for i in range(1, n + 1))


def main():
    n = nhap_n()
    print("So chu so le cua", n, "la:", dem_chu_so_le(n))
    print(f"Tong S = {tinh_tong(n):.6f}")


if __name__ == "__main__":
    main()
