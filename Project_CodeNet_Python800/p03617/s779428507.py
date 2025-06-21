q, h, s, d = map(int, input().split())
n = int(input())
m = min(4 * q, 2 * h, s)
if d / 2 < m:  # d を優先的に使う
    print((n // 2) * d + (n % 2) * m)
else:
    print(n * m)
