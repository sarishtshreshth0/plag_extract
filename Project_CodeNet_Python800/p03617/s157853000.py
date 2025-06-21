q, h, s, d = [int(i) for i in input().split()]
n = int(input())
d = min(min(d, s*2), min(h*4, q*8))
s = min(s, min(h*2, q*4))
h = min(h, q*2)
ans = (n // 2) * d
n %= 2
while n > 0:
    if n >= 1:
        n -= 1
        ans += s
    elif n >= 0.5:
        n -= 0.5
        ans += h
    else:
        n -= 0.25
        ans += q

print(ans)