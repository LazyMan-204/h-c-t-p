"""Cau 2: Xu ly chuoi ky tu."""


def dem_chu_thuong(s):
    return sum(1 for ky_tu in s if ky_tu.islower())


def la_chuoi_doi_xung(s):
    # Bo qua khoang trang va khong phan biet chu hoa/chu thuong.
    chuoi_chuan_hoa = "".join(s.split()).casefold()
    return chuoi_chuan_hoa == chuoi_chuan_hoa[::-1]


def viet_hoa_chu_cai_dau_moi_tu(s):
    # Chi viet hoa ky tu dau, giu nguyen cac ky tu con lai.
    cac_tu = s.split()
    ket_qua = []
    for tu in cac_tu:
        ket_qua.append(tu[0].upper() + tu[1:] if tu else tu)
    return " ".join(ket_qua)


def main():
    s = input("Nhap chuoi s: ")
    print("So ky tu chu thuong:", dem_chu_thuong(s))

    if la_chuoi_doi_xung(s):
        print("Chuoi doi xung.")
    else:
        print("Chuoi khong doi xung.")

    print("Chuoi sau khi viet hoa chu cai dau moi tu:")
    print(viet_hoa_chu_cai_dau_moi_tu(s))


if __name__ == "__main__":
    main()
