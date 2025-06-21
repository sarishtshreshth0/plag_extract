a, b, c, d = map(int, input().split())

if c <= a <= b <= d:
    ans = b - a
elif a <= c <= b <= d:
    ans = b - c
elif c <= a <= d <= b:
    ans = d - a
elif a <= c <= d <= b:
    ans = d - c
else:
    ans = 0

print(ans)