a, b, c, d = map(int, input().split())

lower = max(a, c)
upper = min(b, d)

print(max(0, upper - lower))