# abc124_c.py
# https://atcoder.jp/contests/abc124/tasks/abc124_c

# C - Coloring Colorfully /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 300点

# 問題文
# 左右一列に N枚のタイルが並んでおり、各タイルの初めの色は長さ N の文字列 Sで表されます。
# 左から i番目のタイルは、S の i番目の文字が 0 のとき黒色で、1 のとき白色で塗られています。
# あなたは、いくつかのタイルを黒色または白色に塗り替えることで、どの隣り合う 2枚のタイルも異なる色で塗られているようにしたいです。
# 最小で何枚のタイルを塗り替えることで条件を満たすようにできるでしょうか。

# 制約
#     1≤|S|≤105
#     Siは 0 または 1 である。

# 入力
# 入力は以下の形式で標準入力から与えられる。
# S

# 出力
# 条件を満たすために塗り替えるタイルの枚数の最小値を出力せよ。

# 入力例 1
# 000

# 出力例 1
# 1

# 中央のタイルを白色に塗り替えれば条件を達成できます。

# 入力例 2
# 10010010

# 出力例 2
# 3

# 入力例 3
# 0

# 出力例 3
# 0


global FLAG_LOG
FLAG_LOG = False


def log(value):
    # FLAG_LOG = True
    # FLAG_LOG = False
    if FLAG_LOG:
        print(str(value))


def calculation(lines):
    line = lines[0]
    # N = int(lines[0])
    # values = list(map(int, lines[0].split()))
    # values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[1].split()))
    # values = list()
    # for i in range(6):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(Q):
    #     valueses.append(list(map(int, lines[i+1].split())))

    result = 0

    n_even_kuro = 0
    n_even_shiro = 0
    n_odd_kuro = 0
    n_odd_shiro = 0

    # まず観察
    for i, char in enumerate(line):
        if i % 2 == 0:
            if char == '0':
                n_even_kuro += 1
            else:
                n_even_shiro += 1
        else:
            if char == '0':
                n_odd_kuro += 1
            else:
                n_odd_shiro += 1

    log(n_even_kuro)
    log(n_even_shiro)
    log(n_odd_kuro)
    log(n_odd_shiro)

    # 偶数・奇数それぞれ、黒白どちらが多いかを判断
    dif_even_kuro = n_even_kuro - n_even_shiro
    dif_odd_kuro = n_odd_kuro - n_odd_shiro

    # 偶数=黒/奇数=白 or 偶数=白/奇数=黒 を判断
    if dif_even_kuro > dif_odd_kuro:
        # 偶数=黒/奇数=白
        result = n_even_shiro + n_odd_kuro
    else:
        # 偶数=白/奇数=黒
        result = n_odd_shiro + n_even_kuro

    return [result]


# 引数を取得
def get_input_lines(lines_count):
    lines = list()
    for _ in range(lines_count):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['000']
        lines_export = [1]
    if pattern == 2:
        lines_input = ['10010010']
        lines_export = [3]
    if pattern == 3:
        lines_input = ['0']
        lines_export = [0]
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
        lines_input = get_input_lines(1)
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
