# abc109_b.py
# https://atcoder.jp/contests/abc109/tasks/abc109_b

# B - Shiritori /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# 高橋くんは今日も 1人でしりとりの練習をしています。
# しりとりとは以下のルールで遊ばれるゲームです。
#     はじめ、好きな単語を発言する
#     以降、次の条件を満たす単語を発言することを繰り返す
#         その単語はまだ発言していない単語である
#         その単語の先頭の文字は直前に発言した単語の末尾の文字と一致する
# 高橋くんは、10秒間にできるだけ多くの単語を発言する練習をしています。
# 高橋くんが発言した単語の個数 Nと i 番目に発言した単語 Wiが与えられるので、
# どの発言もしりとりのルールを守っていたかを判定してください。

# 制約
#     Nは 2≤N≤100を満たす整数である
#     Wiは英小文字からなる長さ 1 以上 10以下の文字列である

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N
# W1
# W2
# :
# WN

# 出力
# 高橋くんのどの発言もしりとりのルールを守っていたなら Yes、そうでなければ No を出力せよ。

# 入力例 1
# 4
# hoge
# english
# hoge
# enigma

# 出力例 1
# No

# hoge が複数回発言されているのでしりとりのルールを守っていません。

# 入力例 2
# 9
# basic
# c
# cpp
# php
# python
# nadesico
# ocaml
# lua
# assembly

# 出力例 2
# Yes

# 入力例 3
# 8
# a
# aa
# aaa
# aaaa
# aaaaa
# aaaaaa
# aaa
# aaaaaaa

# 出力例 3
# No

# 入力例 4
# 3
# abc
# arc
# agc

# 出力例 4
# No


def calculation(lines):
    N = int(lines[0])
    # A, B = list(map(int, lines[0].split()))
    last_letter = lines[1][0]
    values = list()
    for i in range(1, N+1):
        line = lines[i]
        if line[0] != last_letter:
            return ['No']
        last_letter = line[-1:]
        if line in values:
            return ['No']
        values.append(line)
    return ['Yes']


# 引数を取得
def get_input_lines():
    line = input()
    N = int(line)
    lines = list()
    lines.append(line)
    for _ in range(N):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['4', 'hoge', 'english', 'hoge', 'enigma']
        lines_export = ['No']
    if pattern == 2:
        lines_input = ['9', 'basic', 'c', 'cpp', 'php', 'python', 'nadesico', 'ocaml', 'lua', 'assembly']
        lines_export = ['Yes']
    if pattern == 3:
        lines_input = ['8', 'a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaa', 'aaaaaaa']
        lines_export = ['No']
    if pattern == 4:
        lines_input = ['3', 'abc', 'arc', 'agc']
        lines_export = ['No']
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
