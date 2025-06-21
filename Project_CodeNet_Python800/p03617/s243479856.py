q, h, s, d = map(int, input().split())
n = int(input())

q *= 4
h *= 2
d_ = d / 2

tmp = min(q, h, s)
ans = 0
if d_ < tmp:
    ans += d * (n // 2)
    ans += tmp * (n % 2)
else:
    ans += n * tmp

print(ans)