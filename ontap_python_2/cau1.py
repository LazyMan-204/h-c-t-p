"""Cau 1: Kiem tra n, tinh tong cac uoc va tinh S."""


def nhap_n():
    while True:
        try:
            n = int(input("Nhap so nguyen duong n (1..99): "))
            if 1 <= n <= 99:
                return n
            print("n phai nam trong doan [1, 99]. Hay nhap lai.")
        except ValueError:
            print("Du lieu khong hop le. Vui long nhap so nguyen.")


def tong_cac_uoc(n):
    """Tra ve tong cac uoc so duong cua n, co tinh ca n."""
    return sum(i for i in range(1, n + 1) if n % i == 0)


def tinh_s(n):
    # S = 1 + 2^2 + 3^3 + ... + n^n
    return sum(i ** i for i in range(1, n + 1))


def main():
    n = nhap_n()
    print(f"Tong cac uoc so cua {n} la: {tong_cac_uoc(n)}")
    print(f"S = {tinh_s(n)}")


if __name__ == "__main__":
    main()
