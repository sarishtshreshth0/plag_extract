q, h, s, d = [int(x) for x in input().split()]
n = int(input())
per_l = min(4 * q, 2 * h, s)   # 1L買うのに一番安い方法
per_2l = min(2 * per_l, d) # 2Lを買うのに一番安い方法

print(per_2l * (n // 2) + per_l * (n % 2))