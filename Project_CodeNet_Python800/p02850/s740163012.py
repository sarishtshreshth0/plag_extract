import sys
from io import StringIO
import unittest
import os
from collections import deque

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


# 実装を行う関数
def resolve(test_def_name=""):
    n = int(input())
    ab_s = [list(map(int, input().split())) for i in range(n - 1)]

    ref_s = [[] for i in range(n + 1)]

    for ab in ab_s:
        ref_s[min(ab)].append(max(ab))

    # deq作成
    que = deque()
    que.appendleft((1, 0))  # 始める場所はどこでもいい。

    ans = {}
    # BFS開始
    while len(que) is not 0:

        pop = que.pop()
        parent = pop[0]
        parent_col = pop[1]

        child_col = 0

        # 繋がる点に移動
        for child in ref_s[parent]:

            child_col += 1
            if child_col == parent_col:
                child_col += 1

            key1 = min(parent, child)
            key2 = max(parent, child)

            # 処理対象のチェック
            # 処理済みなら何もしない
            if ans.get((key1, key2), 0) != 0:
                continue

            # 処理済み状態にする
            ans[(key1, key2)] = child_col

            # 処理対象に対する処理
            # キューに追加(先頭に追加するのでappendleft())
            que.appendleft((child, child_col))

    # 色数を出力
    print(max(ans.values()))

    # 辺の色を出力
    for ab in ab_s:
        key1 = min(ab[0], ab[1])
        key2 = max(ab[0], ab[1])
        print(ans.get((key1, key2)))


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
1 2
2 3"""
        output = """2
1
2"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """8
1 2
2 3
2 4
2 5
4 7
5 6
6 8"""
        output = """4
1
2
3
4
1
1
2"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """6
1 2
1 3
1 4
1 5
1 6"""
        output = """5
1
2
3
4
5"""
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
