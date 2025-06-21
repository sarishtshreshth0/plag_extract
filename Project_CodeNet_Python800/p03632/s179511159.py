a, b, c, d = map(int, input().split())

if b <= c or d <= a:
    ans = 0
elif a < c and c < b and b < d:
    ans = abs(b-c)
elif c < a and a < d and d < b:
    ans = abs(d-a)
elif a <= c and d <= b:
    ans = abs(d-c)
else:
    ans = b-a

print(ans)