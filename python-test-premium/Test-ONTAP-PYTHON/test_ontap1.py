# Đề ôn tập 1 (thư mục ontap_python) - 5 câu x 2 điểm.
# Giá trị mong đợi tính độc lập (phân số/công thức), KHÔNG lấy từ lời giải mẫu.
# "@từ khóa|số" = dòng chứa từ khóa có số cuối cùng bằng số đó (xem autograde.py).
POINTS_PER_BAI = 2

tests = {
    # Câu 1: n trong [1,1500]; đếm chữ số lẻ của n; S = 1/2 + 1/4 + ... + 1/(2n)
    "cau1": [
        {"input": "1\n",    "all": ["@chu so le|1", "@|0.5"]},
        {"input": "15\n",   "all": ["@chu so le|2", "@|1.659114"]},
        {"input": "123\n",  "all": ["@chu so le|2", "@|2.69673"]},
        {"input": "1500\n", "all": ["@chu so le|2", "@|3.945385"]},
    ],

    # Câu 2: đếm chữ hoa; chuỗi đối xứng?; tổng các chữ số
    "cau2": [
        {"input": "Level\n",                       "all": ["@hoa|1", "chuoidoixung",      "@tong|0"]},
        {"input": "Hello World 2025\n",            "all": ["@hoa|2", "chuoikhongdoixung", "@tong|9"]},
        {"input": "A man a plan a canal Panama\n", "all": ["@hoa|2", "chuoidoixung",      "@tong|0"]},
    ],

    # Câu 3: nhập đến khi gặp 0; tổng các số chẵn dương; đếm số lần xuất hiện của k
    "cau3": [
        {"input": "3\n4\n-2\n4\n7\n0\n4\n", "all": ["@chan duong|8",  "@xuat hien|2"]},
        {"input": "0\n5\n",                 "all": ["@chan duong|0",  "@xuat hien|0"]},
        {"input": "2\n-4\n6\n10\n0\n10\n",  "all": ["@chan duong|18", "@xuat hien|1"]},
        {"input": "7\n9\n0\n3\n",           "all": ["@chan duong|0",  "@xuat hien|0"]},
    ],

    # Câu 4: từ điển sách (mã, tên, tác giả, NXB, năm); tìm và xóa theo mã
    # (đề không quy định định dạng in -> chỉ kiểm tra từ khóa)
    "cau4": [
        {"input": "2\nS01\nPython\nAn\nNXB GD\n2020\nS02\nJava\nBinh\nNXB TN\n2021\nS01\n",
         "all": ["S01", "Python", "Java", "xoa"]},
        {"input": "2\nS01\nPython\nAn\nNXB GD\n2020\nS02\nJava\nBinh\nNXB TN\n2021\nS99\n",
         "all": ["Python", "Java", ["khong tim", "khong co"]]},
    ],

    # Câu 5: lớp DienThoai, hai đối tượng mẫu
    "cau5": [
        {"input": "", "all": ["DT01", "iPhone 15 Pro", "Apple", "3274", ["28,990,000", "28990000"],
                              "DT02", "Galaxy S24 Ultra", "Samsung", "5000", ["27,900,000", "27900000"]]},
    ],
}
