q, h, s, d = [int(i) for i in input().split()]
n = int(input())
d = min(min(d, s*2), min(h*4, q*8))
s = min(s, min(h*2, q*4))
print((n // 2) * d + (n % 2) * s)