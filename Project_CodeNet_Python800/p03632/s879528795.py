a, b, c, d = map(int, input().split())
print(len(set(range(a, b)) & set(range(c, d))))