"""Cau 2: Xu ly chuoi - dem chu hoa, doi xung, tong cac chu so."""


def dem_chu_hoa(s):
    return sum(1 for ky_tu in s if ky_tu.isupper())


def la_chuoi_doi_xung(s):
    # Bo qua khoang trang va khong phan biet chu hoa/chu thuong.
    chuoi = "".join(s.lower().split())
    return chuoi == chuoi[::-1]


def tinh_tong_chu_so(s):
    return sum(int(ky_tu) for ky_tu in s if ky_tu.isdigit())


def main():
    s = input("Nhap mot chuoi: ")

    print("So ky tu chu hoa:", dem_chu_hoa(s))
    if la_chuoi_doi_xung(s):
        print("Chuoi doi xung.")
    else:
        print("Chuoi khong doi xung.")
    print("Tong cac chu so trong chuoi:", tinh_tong_chu_so(s))


if __name__ == "__main__":
    main()
