a, b, c, d = map(int, input().split())


lower = max(a, c)
upper = min(b, d)

if upper >= lower:
    print(upper - lower)
else:
    print(0)