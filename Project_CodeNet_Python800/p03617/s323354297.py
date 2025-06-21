q, h, s, d = map(int, input().split())
n = int(input())

m = min(4*q, h*2, s)

tmp = n//2
tmp2 = n % 2
ans1 = tmp * d + tmp2 *m
ans2 = m * n

print(min(ans1, ans2))