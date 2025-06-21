q, h, s, d = map(int, input().split())
n = int(input())

q4 = 4*q
h2 = 2*h

minimum = min(q4, h2, s)

ans = 0
tmp = n//2
tmp2 = n % 2

ans += tmp * d
ans += tmp2 *minimum

ans2 = minimum * n

print(min(ans, ans2))