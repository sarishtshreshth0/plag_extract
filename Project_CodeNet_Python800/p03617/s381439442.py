from sys import stdin

q, h, s, d = map(int, stdin.readline().rstrip().split())
n = int(stdin.readline().rstrip())
q *= 4
h *= 2
t = min(q, h, s)
if 2 * t > d:
    print((n // 2) * d + (n % 2) * t)
else:
    print(n * t)