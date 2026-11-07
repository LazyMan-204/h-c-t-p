"""Cau 4: Quan ly thong tin sach bang tu dien."""


def nhap_sach():
    sach = {}
    try:
        so_luong = int(input("Nhap so luong sach: "))
        if so_luong < 0:
            print("So luong khong duoc am.")
            return sach
    except ValueError:
        print("So luong phai la so nguyen.")
        return sach

    for i in range(so_luong):
        print(f"\nNhap thong tin sach thu {i + 1}:")
        ma_sach = input("Ma so sach: ").strip()
        ten_sach = input("Ten sach: ").strip()
        tac_gia = input("Ten tac gia: ").strip()
        nha_xuat_ban = input("Nha xuat ban: ").strip()
        nam_xuat_ban = input("Nam xuat ban: ").strip()

        sach[ma_sach] = {
            "Ten sach": ten_sach,
            "Tac gia": tac_gia,
            "Nha xuat ban": nha_xuat_ban,
            "Nam xuat ban": nam_xuat_ban,
        }
    return sach


def hien_thi_sach(sach):
    if not sach:
        print("Danh sach sach dang rong.")
        return

    print("\nDANH SACH SACH")
    for ma_sach, thong_tin in sach.items():
        print(f"Ma sach: {ma_sach}")
        for ten_truong, gia_tri in thong_tin.items():
            print(f"  {ten_truong}: {gia_tri}")


def tim_va_xoa_sach(sach):
    ma_can_tim = input("\nNhap ma so sach can tim: ").strip()
    if ma_can_tim in sach:
        print("Thong tin sach tim thay:")
        print("Ma sach:", ma_can_tim)
        for ten_truong, gia_tri in sach[ma_can_tim].items():
            print(f"{ten_truong}: {gia_tri}")
        del sach[ma_can_tim]
        print("Da xoa cuon sach khoi tu dien.")
    else:
        print("Khong tim thay cuon sach can xoa.")


def main():
    sach = nhap_sach()
    hien_thi_sach(sach)
    if sach:
        tim_va_xoa_sach(sach)
        print("\nDanh sach sau khi xu ly:")
        hien_thi_sach(sach)


if __name__ == "__main__":
    main()
