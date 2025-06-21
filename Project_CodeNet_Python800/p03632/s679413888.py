a, b, c, d = map(int, input().split())

if a > c:
    a, c = c, a
if b > d:
    b, d = d, b
ans = b - c
if ans < 0:
    ans = 0

print(ans)