# abc133_b.py
# https://atcoder.jp/contests/abc133/tasks/abc133_b

# B - Good Distance /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# D次元空間上に N個の点があります。
# i番目の点の座標は (Xi1,Xi2,...,XiD)です。
# 座標 (y1,y2,...,yD)の点と座標 (z1,z2,...,zD) の点の距離は √(y1−z1)2+(y2−z2)2+...+(yD−zD)2です。
# i番目の点と j 番目の点の距離が整数となるような組 (i,j) (i<j)はいくつあるでしょうか。

# 制約
#     入力は全て整数である。
#     2≤N≤10
#     1≤D≤10
#     −20≤Xij≤20
#     同じ座標の点は与えられない。すなわち、i≠jならば Xik≠Xjk なる kが存在する。

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N D
# X11 X12 ... X1D
# X21 X22 ... X2D
# ⋮
# XN1 XN2 ... XND

# 出力
# i番目の点と j 番目の点の距離が整数となるような組 (i,j) (i<j)の数を出力せよ。

# 入力例 1
# 3 2
# 1 2
# 5 5
# -2 8

# 出力例 1
# 1

# 以下のように距離が整数となる点の組は 1組です。
#     1番目の点と 2 番目の点の距離は √|1−5|2+|2−5|2=5で、これは整数です。
#     2番目の点と 3 番目の点の距離は √|5−(−2)|2+|5−8|2=√58で、これは整数ではありません。
#     3番目の点と 1 番目の点の距離は √|−2−1|2+|8−2|2=3√5で、これは整数ではありません。

# 入力例 2
# 3 4
# -3 7 8 2
# -12 1 10 2
# -2 8 9 3

# 出力例 2
# 2

# 入力例 3
# 5 1
# 1
# 2
# 3
# 4
# 5

# 出力例 3
# 10


global FLAG_LOG
FLAG_LOG = False


def log(value):
    # FLAG_LOG = True
    # FLAG_LOG = False
    if FLAG_LOG:
        print(str(value))


def calculation(lines):
    # S = lines[0]
    # N = int(lines[0])
    N, D = list(map(int, lines[0].split()))
    # values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(6):
    #     values.append(int(lines[i]))
    valueses = list()
    for i in range(N):
        valueses.append(list(map(int, lines[i+1].split())))

    cnt = 0
    for n1 in range(N-1):
        for n2 in range(n1+1, N):
            log(f'n1=[{n1}], n2=[{n2}]')
            d = 0
            for dd in range(D):
                d += (valueses[n1][dd] - valueses[n2][dd])**2
            d = d**0.5
            if d == float(int(d)):
                cnt += 1

    return [cnt]


# 引数を取得
def get_input_lines():
    line = input()
    N, D = list(map(int, line.split()))
    lines = list()
    lines.append(line)
    for _ in range(N):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['3 2', '1 2', '5 5', '-2 8']
        lines_export = [1]
    if pattern == 2:
        lines_input = ['3 4', '-3 7 8 2', '-12 1 10 2', '-2 8 9 3']
        lines_export = [2]
    if pattern == 3:
        lines_input = ['5 1', '1', '2', '3', '4', '5']
        lines_export = [10]
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
        lines_input = get_input_lines()
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
