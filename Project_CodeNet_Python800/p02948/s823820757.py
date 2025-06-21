import sys
from io import StringIO
import unittest
import os
import heapq

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


# 実装を行う関数
def resolve(test_def_name=""):
    n, m = map(int, input().split())
    ab_s = [list(map(int, input().split())) for i in range(n)]

    # 支給日ごとの報酬(降順)をまとめたリストを作成する。
    # 支給日が1日後:10,4,2円・・ 支給日が3日後:100,50円・・の場合 =  1[2,4,10] 3[50,100]　という感じ。
    # 降順にしておけば、取り出したい値=最大値が末尾にくるので、
    # 後述のキュー処理に要する処理量を抑えることができる。(list.pop()を使えるので)
    ab_list = [[] for i in range(100001)]
    for i in ab_s:
        ab_list[i[0]].append(i[1])
    for i in ab_list:
        if len(i) == 0:
            continue
        i.sort()

    a = []
    heapq.heapify(a)

    ans = 0
    # 　最適なバイトを、制限の多い地点から決めていく。(今回は、日が進むごとに制限が増えるので、
    # 　最も制限の多い最終日->最も制限のない1日目の順に決める)
    for i in range(1, m + 1):
        # (給与,支給日)の形でキューに追加。
        if len(ab_list[i]) != 0:
            heapq.heappush(a, (-ab_list[i].pop(), i))

        if len(a) != 0:
            act_work = heapq.heappop(a)
            ans += -act_work[0]

            if len(ab_list[act_work[1]]) != 0:
                heapq.heappush(a, (-ab_list[act_work[1]].pop(), act_work[1]))

    print(ans)


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
        test_input = """3 4
4 3
4 1
2 2"""
        output = """5"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """5 3
1 2
1 3
1 4
2 1
2 3"""
        output = """10"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """1 1
2 1"""
        output = """0"""
        self.assertIO(test_input, output)

    # 自作テストパターンのひな形(利用時は「tes_t」のアンダーバーを削除すること
    def test_original_1(self):
        test_input = """3 4
4 210
4 150
3 150"""
        output = """360"""
        self.assertIO(test_input, output)

    def test_original_2(self):
        test_input = """2 1
1 10
1 20
"""
        output = """20"""
        self.assertIO(test_input, output)

    def test_original_3(self):
        test_input = """1 2
1 10
"""
        output = """10"""
        self.assertIO(test_input, output)

    def test_original_4(self):
        test_input = """5 3
4 50
4 50
3 10
3 10
1 10
"""
        output = """20"""
        self.assertIO(test_input, output)


# 実装orテストの呼び出し
if __name__ == "__main__":
    if os.environ.get("USERNAME") is None:
        # AtCoder提出時の場合
        resolve()

    else:
        # 自PCの場合
        unittest.main()
