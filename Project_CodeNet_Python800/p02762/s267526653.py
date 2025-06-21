import sys
from io import StringIO
import unittest
import os


# union find木
# 参考：https://note.nkmk.me/python-union-find/
class UnionFind:
    def __init__(self, n):
        """
        コンストラクタ
        :要素数 n:
        """
        self.n = n
        # 添字x: 値yとすると・・
        #   root以外の場合： 要素xは集合yに所属する。
        #   rootの場合　　　： 集合xの要素数はy個である。(負数で保持する)
        self.parents = [-1] * n

    def getroot(self, x):
        """
        所属する集合(ルートの番号)を取得する。
        :調査する要素 x:
        """
        # 値が負数 = ルートに到達したので、ルート木の番号を返す。
        if self.parents[x] < 0:
            return x
        else:
            # 値が正数 = ルートに到達していない場合、さらに親の情報を確認する。
            # 下の行は経路圧縮の処理。
            self.parents[x] = self.getroot(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """
        2つの要素が所属する集合をを同じ集合に結合する。
        :結合する要素(1つ目) x:
        :結合する要素(2つ目) y:
        """
        # 既に同じ集合に存在するなら何もせず終了。
        x = self.getroot(x)
        y = self.getroot(y)
        if x == y:
            return

        # 集合を結合する。
        # ※ここ、「要素数の大きい集合に、少ない集合を結合」しているが、こうすることで以後の「処理量を削減」するテクニックである。
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        """
        指定した集合に属する要素数を取得する。
        :調査する集合 x:
        """
        # 添え字[root]には、要素数が負数で格納されている。そのため、取得する際は-反転する。
        return -self.parents[self.getroot(x)]

    def is_same(self, x, y):
        return self.getroot(x) == self.getroot(y)

    def members(self, x):
        root = self.getroot(x)
        return [i for i in range(self.n) if self.getroot(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


# 実装を行う関数
def resolve():
    # 数値取得サンプル
    #   1行N項目 x, y = map(int, input().split())
    #   N行N項目 x = [list(map(int, input().split())) for i in range(n)]
    n, m, k = map(int, input().split())
    friends = [list(map(int, input().split())) for i in range(m)]
    blocks = [list(map(int, input().split())) for i in range(k)]

    # uf 作成(要素数を+1しているのは添え字と人番号を合わせるため)
    uf = UnionFind(n + 1)

    # 除外リスト作成(これは、本問題特有の処理)
    # 添字x: 値yとすると・・ 要素xの友達候補を数えるとき、y(list)に該当する人は除外する。(要素数を+1しているのは添え字と人番号を合わせるため)
    omits = [[] for i in range(n + 1)]

    # UnionFindにて集合を明確にする。
    for friend in friends:
        uf.union(friend[0], friend[1])

        # 除外リストを更新(これは、本問題特有の処理)
        omits[friend[0]].append(friend[1])
        omits[friend[1]].append(friend[0])

    # ブロックリストの情報を除外リストに加える(これは、本問題特有の処理)
    for block in blocks:
        # 同じ集合に属するウ場合のみ、リストに追加
        if uf.is_same(block[0], block[1]):
            omits[block[0]].append(block[1])
            omits[block[1]].append(block[0])

    # 友達候補数を出力して終了(人は1始まりなので1からループを行う
    # ans = []
    # for i in range(1, n + 1):
        # 友達候補 = 集合数 - 除外リスト(自分の友人数 + 自分がブロックしている人数) - 1(集合に含まれる自分自身を除く)
    #     ans.append(uf.size(i) - len(omits[i]) - 1)
    # print(" ".join(ans))

    # ans = [str(uf.size(i) - len(omits[i]) - 1) for i in range(1, n + 1)]
    ans = [uf.size(i) - len(omits[i]) - 1 for i in range(1, n + 1)]

    print(*ans)


# テストクラス
class TestClass(unittest.TestCase):
    def assertIO(self, assert_input, output):
        stdout, sat_in = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(assert_input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, sat_in
        self.assertEqual(out, output)

    def test_input_1(self):
        test_input = """4 4 1
2 1
1 3
3 2
3 4
4 1"""
        output = """0 1 0 1"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """5 10 0
1 2
1 3
1 4
1 5
3 2
2 4
2 5
4 3
5 3
4 5"""
        output = """0 0 0 0 0"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """10 9 3
10 1
6 7
8 2
2 5
8 4
7 3
10 9
6 4
5 8
2 6
7 5
3 1"""
        output = """1 3 5 4 3 3 3 3 1 0"""
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
