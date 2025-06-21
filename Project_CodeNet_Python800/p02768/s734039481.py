# -*- coding: utf-8 -*-
n, a, b = map(int, input().split())
p = 10**9 + 7

# 全組み合わせ 2**n % (10**9 + 7) から1本も選択しない1パターンを引いている
x = pow(2, n, p) - 1

# nCa % (10**9 + 7)
y = 1
z = 1
for i in range(1, a+1):
  y = y * (n - i + 1) % p
  z = z * i % p
n_c_a = y * pow(z, p-2, p) % p

# nCb % (10**9 + 7)
y = 1
z = 1
for i in range(1, b+1):
  y = y * (n - i + 1) % p
  z = z * i % p
n_c_b = y * pow(z, p-2, p) % p

print((x - n_c_a - n_c_b) % p)