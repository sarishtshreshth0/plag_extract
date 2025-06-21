# abc109_c.py
# https://atcoder.jp/contests/abc109/tasks/abc109_c

# C - Skip /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 300点

# 問題文
# 数直線上に N個の都市があり、i 番目の都市は座標 xiにあります。
# あなたの目的は、これら全ての都市を 1度以上訪れることです。
# あなたは、はじめに正整数 Dを設定します。
# その後、あなたは座標 Xから出発し、以下の移動 1、移動 2を好きなだけ行います。
#     移動 1: 座標 y から座標 y+Dに移動する
#     移動 2: 座標 y から座標 y−Dに移動する
# 全ての都市を 1度以上訪れることのできる Dの最大値を求めてください。
# ここで、都市を訪れるとは、その都市のある座標に移動することです。

# 制約
#     入力はすべて整数である
#     1≤N≤10^5
#     1≤X≤10^9
#     1≤xi≤10^9
#     xiはすべて異なる
#     x1,x2,...,xN≠X

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N X
# x1 x2 ... xN

# 出力
# 全ての都市を 1度以上訪れることのできる Dの最大値を出力せよ。

# 入力例 1
# 3 3
# 1 7 11

# 出力例 1
# 2

# D=2と設定すれば次のように移動を行うことですべての都市を訪れることができ、これが最大です。

#     移動 2を行い、座標 1に移動する
#     移動 1を行い、座標 3に移動する
#     移動 1を行い、座標 5に移動する
#     移動 1を行い、座標 7に移動する
#     移動 1を行い、座標 9に移動する
#     移動 1を行い、座標 11に移動する

# 入力例 2
# 3 81
# 33 105 57

# 出力例 2
# 24

# 入力例 3
# 1 1
# 1000000000

# 出力例 3
# 999999999


def calculation(lines):
    # N = int(lines[0])
    N, X = list(map(int, lines[0].split()))
    values = list(map(int, lines[1].split()))
    values.append(X)
    mi = min(values)
    # 最小値を起点とする
    values = [value - mi for value in values]

    for _ in range(10):
        # 解の候補として最小値を取得する
        values = [value for value in values if value > 0]
        mi = min(values)
        # 最小値単位のあまりを取得する
        values = list(set([value % mi for value in values]))
        if values == [0]:
            return [mi]


# 引数を取得
def get_input_lines(lines_count):
    lines = list()
    for _ in range(lines_count):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['3 3', '1 7 11']
        lines_export = [2]
    if pattern == 2:
        lines_input = ['3 81', '33 105 57']
        lines_export = [24]
    if pattern == 3:
        lines_input = ['1 1', '1000000000']
        lines_export = [999999999]
    return lines_input, lines_export


# 動作モード判別
def get_mode():
    import sys
    args = sys.argv
    if len(args) == 1:
        mode = 0
    else:
        mode = int(args[1])
    return mode


# 主処理
def main():
    import time
    started = time.time()
    mode = get_mode()
    if mode == 0:
        lines_input = get_input_lines(2)
    else:
        lines_input, lines_export = get_testdata(mode)

    lines_result = calculation(lines_input)

    for line_result in lines_result:
        print(line_result)

    # if mode > 0:
    #     print(f'lines_input=[{lines_input}]')
    #     print(f'lines_export=[{lines_export}]')
    #     print(f'lines_result=[{lines_result}]')
    #     if lines_result == lines_export:
    #         print('OK')
    #     else:
    #         print('NG')
    # finished = time.time()
    # duration = finished - started
    # print(f'duration=[{duration}]')


# 起動処理
if __name__ == '__main__':
    main()
