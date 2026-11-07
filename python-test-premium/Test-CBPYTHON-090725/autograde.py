# -*- coding: utf-8 -*-
"""Chấm bài tự động.  Cách dùng (chạy trong thư mục chứa file này):

    python autograde.py de1            # chấm thư mục submissions_de1 với test_de1.py
    python autograde.py de2 sv001      # chấm submissions_de2, ghi mã SV

Quy ước trong test_deX.py (mỗi test case là một dict):
    "input":    chuỗi đưa vào stdin
    "expected": [a, b, ...]  -> ĐÚNG nếu khớp BẤT KỲ giá trị nào (các cách in khác nhau)
    "all":      [a, b, ...]  -> ĐÚNG chỉ khi khớp TẤT CẢ (câu yêu cầu in nhiều kết quả)
    "exact":    True         -> phải trùng nguyên văn một dòng (phân biệt hoa/thường, dấu cách)
  Mỗi giá trị trong expected/all có thể là:
    "30", "(1, 2)", "True", "text"  -> như trên (số / cấu trúc Python / văn bản)
    "==Hello World"                 -> một dòng phải trùng nguyên văn
    "@tu khoa|12"                   -> có dòng chứa "tu khoa" mà SỐ CUỐI CÙNG trên dòng = 12
                                       (hợp với chương trình dùng input("Nhap ...: ") vì lời nhắc dính vào dòng kết quả;
                                       số thực cho phép sai lệch 0.006; để trống từ khóa: "@|12" = dòng bất kỳ)
    ["a", "b"]  (list, chỉ trong "all") -> khớp bất kỳ giá trị nào trong list đó
Có thể khai báo POINTS_PER_BAI ở đầu test_deX.py (mặc định = 10 / số bài).
"""
import ast
import importlib
import os
import re
import subprocess
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def strip_accents(s):
    s = s.replace("đ", "d").replace("Đ", "D")
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def normalize(s):
    s = strip_accents(str(s)).lower()
    return re.sub(r"[\s:=]", "", s)


def run_code(file, input_data):
    env = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8")
    try:
        r = subprocess.run(
            [sys.executable, file], input=input_data.encode("utf-8"),
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            timeout=3, env=env, cwd=os.path.dirname(file),
        )
    except subprocess.TimeoutExpired:
        return ["loiquathoigian"]
    out = r.stdout.decode("utf-8", errors="replace").splitlines()
    return [l.strip() for l in out if l.strip()]


NUM = r"-?\d+(?:\.\d+)?"


def match(item, lines, exact=False):
    if isinstance(item, (list, tuple)):          # any-of lồng trong "all"
        return any(match(x, lines, exact) for x in item)
    item = str(item)
    if item.startswith("=="):                    # nguyên văn một dòng
        return any(l == item[2:] for l in lines)
    if item.startswith("@") and "|" in item:     # "@từ khóa|số cuối dòng"
        kw, val = item[1:].rsplit("|", 1)
        want = float(val)
        tol = 0.006 if "." in val else 0
        for l in lines:
            if normalize(kw) in normalize(l):
                nums = re.findall(NUM, l)
                if nums and abs(float(nums[-1]) - want) <= tol:
                    return True
        return False
    if exact:
        return any(l == item for l in lines)
    # 1) số: so sánh theo từng số trọn vẹn ("30" không khớp "130" hay "2000")
    if re.fullmatch(NUM, item.strip()):
        want = float(item)
        return any(float(t) == want for l in lines for t in re.findall(NUM, l))
    # 2) cấu trúc Python (set/dict/tuple/list/bool...): so sánh giá trị, không phụ thuộc thứ tự in
    try:
        want = ast.literal_eval(item)
    except Exception:
        want = None
    else:
        for l in lines:
            try:
                got = ast.literal_eval(l)
            except Exception:
                continue
            if type(got) is type(want) and got == want:
                return True
    # 3) văn bản: không phân biệt hoa/thường, dấu cách, dấu tiếng Việt
    n = normalize(item)
    return any(n in normalize(l) for l in lines)


def case_ok(test, out):
    if "all" in test:
        return all(match(x, out, test.get("exact")) for x in test["all"])
    exp = test["expected"]
    exp = [exp] if isinstance(exp, str) else exp
    return any(match(x, out, test.get("exact")) for x in exp)


def grade(de, student_id="sv001"):
    mod = importlib.import_module(f"test_{de}")
    tests = mod.tests
    pts = getattr(mod, "POINTS_PER_BAI", 10 / len(tests))
    base = os.path.join(HERE, f"submissions_{de}")
    total = 0.0
    print(f"📋 Bắt đầu chấm điểm cho {student_id} ({de})\n")
    for bai, cases in tests.items():
        path = os.path.join(base, f"{bai}.py")
        if not os.path.exists(path):
            print(f"❌ Không tìm thấy file: {path}\n")
            continue
        print(f"🔹 {bai.upper()}")
        right = 0
        for i, t in enumerate(cases, 1):
            ok = case_ok(t, run_code(path, t["input"]))
            right += ok
            print(f"  {'✅' if ok else '❌'} Test {i}: Input {t['input'].strip()!r} → {'Đúng' if ok else 'Sai'}")
        score = round(pts * right / len(cases), 2)
        total += score
        print(f"    Kết quả: {right}/{len(cases)} test đúng → {score} điểm\n")
    mx = round(pts * len(tests), 2)
    print(f"🎯 Tổng điểm: {round(total, 2)}/{mx}   |   SV: {student_id}   |   Đề: {de}")
    return total


if __name__ == "__main__":
    grade(sys.argv[1] if len(sys.argv) > 1 else "de1", sys.argv[2] if len(sys.argv) > 2 else "sv001")
