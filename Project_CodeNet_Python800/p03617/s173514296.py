import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

a, b, c, d, N = map(int, read().split())

b = min(a + a, b)
c = min(b + b, c)
d = min(c + c, d)

q, r = divmod(N, 2)
x = q * d + r * c
print(x)