# h-c-t-p: Bộ chấm bài Python tự động

Bộ công cụ chấm các đề kiểm tra và đề ôn tập Python. Mỗi câu của sinh viên là một file `.py`; chương trình chạy file đó với dữ liệu nhập mẫu, so kết quả in ra với đáp án mong đợi rồi tính điểm.

## Cấu trúc

```
python-test-premium/
├── Test-CBPYTHON-090725/     Đề Cơ bản (2 đề, 10 câu nhỏ/đề, 1 điểm/câu)
├── Test-NCPYTHON-090725/     Đề NC (2 đề, 6 câu nhỏ/đề, 1,5 điểm/câu)
├── Test-NDPYTHON-090725/     Đề ND (2 đề, 6 câu nhỏ/đề, 1,5 điểm/câu)
└── Test-ONTAP-PYTHON/        2 đề ôn tập (5 câu/đề, 2 điểm/câu)
```

Trong mỗi thư mục có:

| File / thư mục | Vai trò |
| --- | --- |
| `autograde.py` | Chương trình chấm điểm (dùng chung cho mọi bộ) |
| `test_de1.py`, `test_de2.py` | Dữ liệu test của đề 1, đề 2 (bộ ôn tập: `test_ontap1.py`, `test_ontap2.py`) |
| `submissions_de1/`, `submissions_de2/` | Bài làm cần chấm (bộ ôn tập: `submissions_ontap1/`, `submissions_ontap2/`) |

## Cách chạy

Yêu cầu: Python 3.8 trở lên, không cần cài thêm thư viện.

Mở terminal **trong thư mục của bộ cần chấm** rồi chạy `autograde.py` kèm tên đề:

```bash
cd python-test-premium/Test-CBPYTHON-090725
python autograde.py de1            # chấm submissions_de1 bằng test_de1.py
python autograde.py de2 sv001      # chấm đề 2, ghi mã sinh viên sv001

cd ../Test-ONTAP-PYTHON
python autograde.py ontap1
python autograde.py ontap2
```

Chú ý: chạy `autograde.py` (không chạy trực tiếp `test_*.py`, các file đó chỉ chứa dữ liệu). Nếu lệnh `python` không được, dùng `py autograde.py de1` trên Windows.

Tên file bài làm phải đúng như trong file test, ví dụ `Cau1a.py`, `Cau2b.py` (bộ CB, NC, ND) hoặc `cau1.py` đến `cau5.py` (bộ ôn tập).

## Cách chấm

- Mỗi bài chạy với từng bộ dữ liệu nhập trong file test (giới hạn 3 giây). Điểm của bài = điểm tối đa × (số test đúng / tổng số test).
- Số, set, dict, tuple, list và True/False được so theo giá trị, nên thứ tự in không ảnh hưởng.
- Văn bản được so không phân biệt hoa/thường, khoảng trắng và dấu tiếng Việt.

## Viết test mới

Mỗi bài là một danh sách các test case trong `tests = {...}`:

```python
POINTS_PER_BAI = 1          # điểm tối đa của mỗi bài (không khai báo = 10 / số bài)

tests = {
    "Cau1a": [
        {"input": "4\n", "expected": ["chan"]},          # đúng nếu khớp BẤT KỲ giá trị nào
        {"input": "", "all": ["apple", "cherry"]},        # đúng chỉ khi khớp TẤT CẢ
    ],
}
```

| Khóa / giá trị | Ý nghĩa |
| --- | --- |
| `"expected": [a, b]` | Khớp bất kỳ giá trị nào (các cách in khác nhau đều được) |
| `"all": [a, b]` | Phải khớp tất cả (dùng khi đề yêu cầu in nhiều kết quả) |
| `"exact": True` | Phải trùng nguyên văn một dòng, phân biệt hoa/thường |
| `"==Hello World"` | Giá trị này phải trùng nguyên văn một dòng |
| `"@tu khoa\|12"` | Có dòng chứa `tu khoa` mà số cuối cùng trên dòng bằng 12 (hợp với `input("Nhap...: ")` vì lời nhắc dính vào dòng kết quả; số thực cho phép lệch 0,006) |
| `["a", "b"]` trong `"all"` | Khớp bất kỳ giá trị nào trong list con đó |

## Lưu ý

- Giá trị mong đợi của bộ ôn tập được tính độc lập với lời giải mẫu. Dữ liệu mẫu của câu 4 và câu 5 lấy từ lời giải, nên hãy đối chiếu với đề thật.
- Không đưa mật khẩu, token hay file nhạy cảm vào thư mục trước khi đẩy lên GitHub.
