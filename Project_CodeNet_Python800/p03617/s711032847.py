q, h, s, d = map(int, input().split())
n = int(input())
m = min(4*q, 2*h, s)
if n % 2:
    print(min(d * (n//2) + m, m * n))
else:
    print(min(d * (n//2), m * n))