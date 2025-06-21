q, h, s, d = [int(i) for i in input().split()]
n = int(input())
s = min(s, min(h*2, q*4))
d = min(d, s*2)
print((n // 2) * d + (n % 2) * s)