# -*- coding: utf-8 -*-

# ハーシャッド数

N = int(input())
N_l = list(str(N))
h_x = 0

for x in N_l:
    h_x = h_x + int(x)

if N % h_x == 0:
    print('Yes')
else:
    print('No')