a, b, c, d = map(int, input().split())
x = len(set(range(a, b + 1)) & set(range(c, d + 1))) - 1
print(x if x >= 0 else 0)