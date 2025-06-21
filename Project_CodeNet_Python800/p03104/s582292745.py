# [1〜A - 1のXOR]と[1〜BのXOR]のXORが答え
# mod 4が3になる数でXORは0になるので、A(B)より小さい最大の4の倍数からA(B)までのXORだけ取ればよい

import sys
readline = sys.stdin.readline

A,B = map(int,readline().split())
a = 0
for i in range(((A - 1) // 4) * 4,A):
  a ^= i
  
b = 0
for i in range((B // 4) * 4,B + 1):
  b ^= i

print(a ^ b)
