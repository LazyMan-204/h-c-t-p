"""Cau 5: Xay dung lop MonHoc."""


class MonHoc:
    def __init__(self, ma_mon_hoc, ten_mon_hoc, so_tin_chi, khoa_phu_trach):
        self.MaMonHoc = ma_mon_hoc
        self.TenMonHoc = ten_mon_hoc
        self.SoTinChi = so_tin_chi
        self.KhoaPhuTrach = khoa_phu_trach

    def thongtinmonhoc(self):
        print("Ma mon hoc:", self.MaMonHoc)
        print("Ten mon hoc:", self.TenMonHoc)
        print("So tin chi:", self.SoTinChi)
        print("Khoa phu trach:", self.KhoaPhuTrach)


def main():
    mon_hoc_1 = MonHoc(
        229008,
        "Co so du lieu",
        3,
        "Cong nghe thong tin"
    )

    mon_hoc_2 = MonHoc(
        224604,
        "Tieng Anh 1",
        2,
        "Ngoai ngu"
    )

    print("Thong tin mon hoc thu nhat:")
    mon_hoc_1.thongtinmonhoc()

    print("\nThong tin mon hoc thu hai:")
    mon_hoc_2.thongtinmonhoc()


if __name__ == "__main__":
    main()
