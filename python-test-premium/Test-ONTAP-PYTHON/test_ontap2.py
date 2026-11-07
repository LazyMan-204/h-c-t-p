# Đề ôn tập 2 (thư mục ontap_python_2) - 5 câu x 2 điểm.
POINTS_PER_BAI = 2

tests = {
    # Câu 1: n trong [1,99]; tổng các ước của n (kể cả n); S = 1 + 2^2 + 3^3 + ... + n^n
    "cau1": [
        {"input": "6\n",  "all": ["@uoc|12", "@|50069"]},
        {"input": "7\n",  "all": ["@uoc|8",  "@|873612"]},
        {"input": "10\n", "all": ["@uoc|18", "@|10405071317"]},
    ],

    # Câu 2: đếm chữ thường; chuỗi đối xứng?; viết hoa chữ cái đầu mỗi từ
    "cau2": [
        {"input": "hello world\n",                 "all": ["@thuong|10", "chuoikhongdoixung", "==Hello World"]},
        {"input": "Level\n",                       "all": ["@thuong|4",  "chuoidoixung",      "==Level"]},
        {"input": "A man a plan a canal Panama\n", "all": ["@thuong|19", "chuoidoixung",      "==A Man A Plan A Canal Panama"]},
        {"input": "xin chao viet nam\n",           "all": ["@thuong|14", "chuoikhongdoixung", "==Xin Chao Viet Nam"]},
    ],

    # Câu 3: nhập đến khi gặp 0; in các số dương chẵn; đếm số lần xuất hiện của k
    "cau3": [
        {"input": "3\n4\n-2\n6\n4\n0\n4\n", "all": [["[4, 6, 4]", "4 6 4"], "@xuat hien|2"]},
        {"input": "0\n5\n",                 "all": ["[]", "@xuat hien|0"]},
        {"input": "-2\n-8\n7\n0\n7\n",      "all": ["[]", "@xuat hien|1"]},
    ],

    # Câu 4: từ điển máy tính (số hiệu, bộ nhớ, ổ cứng, hãng, năm); tìm và xóa theo số hiệu
    "cau4": [
        {"input": "1\nM01\n8GB\n512GB\nDell\n2022\nM01\n",
         "all": ["M01", "Dell", "512GB", "8GB", "xoa"]},
        {"input": "1\nM01\n8GB\n512GB\nDell\n2022\nM99\n",
         "all": ["Dell", ["khong co", "khong tim"]]},
    ],

    # Câu 5: lớp MonHoc, hai đối tượng mẫu
    "cau5": [
        {"input": "", "all": ["229008", "Co so du lieu", "3", "Cong nghe thong tin",
                              "224604", "Tieng Anh 1", "2", "Ngoai ngu"]},
    ],
}
