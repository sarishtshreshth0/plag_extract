# abc129_b.py
# https://atcoder.jp/contests/abc129/tasks/abc129_b

# B - Balance /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# 1から N の番号がついた N 個の重りがあり、番号 i の重りの重さは Wiです。
# ある整数 1≤T<Nに対してこれらの重りを、番号が T 以下の重り と 番号が T より大きい重りの 2 グループに分けることを考え、
# それぞれのグループの重さの和を S1,S2とします。
# このような分け方全てを考えた時、S1と S2の差の絶対値の最小値を求めてください。

# 制約
#     2≤N≤100
#     1≤Wi≤100
#     入力は全て整数である

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N
# W1 W2 ... WN−1 WN

# 出力
# S1と S2の差の絶対値の最小値を出力せよ。

# 入力例 1
# 3
# 1 2 3

# 出力例 1
# 0

# T=2としたとき、S1=1+2=3,S2=3 となり、差の絶対値は 0となります。

# 入力例 2
# 4
# 1 3 1 1

# 出力例 2
# 2

# T=2としたとき、S1=1+3=4,S2=1+1=2 となり、差の絶対値は 2です。これより差の絶対値を小さくすることは出来ません。

# 入力例 3
# 8
# 27 23 76 2 3 5 62 52

# 出力例 3
# 2


global FLAG_LOG
FLAG_LOG = False


def log(value):
    # FLAG_LOG = True
    # FLAG_LOG = False
    if FLAG_LOG:
        print(str(value))


def calculation(lines):
    # S = lines[0]
    N = int(lines[0])
    # N, M = list(map(int, lines[0].split()))
    values = list(map(int, lines[1].split()))
    # values_p = list(map(int, lines[M+1].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(M):
    #     valueses.append(list(map(int, lines[i+1].split())))

    mi = None

    for n in range(N):
        a = sum(values[:n])
        b = sum(values[n:])
        dif = abs(a-b)
        if mi is None:
            mi = dif
        elif mi > dif:
            mi = dif

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
        lines_input = ['3', '1 2 3']
        lines_export = [0]
    if pattern == 2:
        lines_input = ['4', '1 3 1 1']
        lines_export = [2]
    if pattern == 3:
        lines_input = ['8', '27 23 76 2 3 5 62 52']
        lines_export = [2]
    return lines_input, lines_export


# 動作モード判別
def get_mode():
    import sys
    args = sys.argv
    global FLAG_LOG
    if len(args) == 1:
        mode = 0
        FLAG_LOG = False
    else:
        mode = int(args[1])
        FLAG_LOG = True
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
