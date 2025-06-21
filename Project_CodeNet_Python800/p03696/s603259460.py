# 括弧が開いている数を左からカウント
# "("が0の状態で")"が来たらopen状態は変えずにその数をカウント・・・A
# 最終的にかっこが開いている数をカウント・・・B
# Aの数だけ"("を左端に追加
# Bの数だけ")"を右端に追加

import sys
readline = sys.stdin.readline

N = int(readline())
S = readline().rstrip()

open = 0
a = 0
for i in range(len(S)):
  if S[i] == "(":
    open += 1
  else:
    if open == 0:
      a += 1
    else:
      open -= 1

print(a * "(" + S + ")" * open)
