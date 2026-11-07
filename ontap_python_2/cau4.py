"""Cau 4: Quan ly thong tin may tinh bang tu dien."""


def nhap_thong_tin_may_tinh():
    so_hieu = input("Nhap so hieu may tinh: ").strip()
    dung_luong_bo_nho = input("Nhap dung luong bo nho: ").strip()
    dung_luong_o_cung = input("Nhap dung luong o cung: ").strip()
    hang_san_xuat = input("Nhap hang san xuat: ").strip()
    nam_san_xuat = input("Nhap nam san xuat: ").strip()

    return so_hieu, {
        "Dung luong bo nho": dung_luong_bo_nho,
        "Dung luong o cung": dung_luong_o_cung,
        "Hang san xuat": hang_san_xuat,
        "Nam san xuat": nam_san_xuat,
    }


def hien_thi_may_tinh(so_hieu, thong_tin):
    print(f"\nThong tin may tinh co so hieu {so_hieu}:")
    for ten_thuoc_tinh, gia_tri in thong_tin.items():
        print(f"- {ten_thuoc_tinh}: {gia_tri}")


def main():
    danh_sach_may_tinh = {}

    try:
        so_luong = int(input("Nhap so luong may tinh: "))
        if so_luong < 0:
            print("So luong khong duoc am.")
            return
    except ValueError:
        print("So luong khong hop le.")
        return

    for i in range(so_luong):
        print(f"\nNhap may tinh thu {i + 1}:")
        so_hieu, thong_tin = nhap_thong_tin_may_tinh()
        danh_sach_may_tinh[so_hieu] = thong_tin

    print("\nTu dien may tinh:", danh_sach_may_tinh)
    can_tim = input("\nNhap so hieu may tinh can tim: ").strip()

    if can_tim in danh_sach_may_tinh:
        hien_thi_may_tinh(can_tim, danh_sach_may_tinh[can_tim])
        del danh_sach_may_tinh[can_tim]
        print("Da xoa may tinh khoi tu dien.")
    else:
        print("Khong co may tinh can tim.")

    print("Tu dien sau khi xu ly:", danh_sach_may_tinh)


if __name__ == "__main__":
    main()
