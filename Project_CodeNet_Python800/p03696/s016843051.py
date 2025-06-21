import sys
from io import StringIO
import unittest
import os

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


# 実装を行う関数
def resolve(test_def_name=""):
    n = int(input())
    s_s = list(input())

    # work_s = str(s)

    for i in range(101):
        j = 0
        c = 0
        for cnt, s in enumerate(s_s):
            if s == "(":
                c += 1
            else:
                j += 1
            if c < j:
                s_s = ["("] + s_s
                break
            if cnt == len(s_s) - 1 and c > j:
                s_s = s_s + [")"]

    print("".join(s_s))
        # work_s = work_s.replace("()", "1")
        #
        # if i == 0:
        #     for j in range(100):
        #         work_s = work_s.replace("(X)", "X")
        # else:
        #     work_s = work_s.replace("(X)", "X")

        # テストクラス


class TestClass(unittest.TestCase):
    def assertIO(self, assert_input, output):
        stdout, sat_in = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(assert_input)
        resolve(sys._getframe().f_back.f_code.co_name)
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, sat_in
        self.assertEqual(out, output)

    def test_input_1(self):
        test_input = """3
())"""
        output = """(())"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """6
)))())"""
        output = """(((()))())"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """8
))))(((("""
        output = """(((())))(((())))"""
        self.assertIO(test_input, output)

    # 自作テストパターンのひな形(利用時は「tes_t」のアンダーバーを削除すること
    def tes_t_1original_1(self):
        test_input = """データ"""
        output = """データ"""
        self.assertIO(test_input, output)


# 実装orテストの呼び出し
if __name__ == "__main__":
    if os.environ.get("USERNAME") is None:
        # AtCoder提出時の場合
        resolve()

    else:
        # 自PCの場合
        unittest.main()
