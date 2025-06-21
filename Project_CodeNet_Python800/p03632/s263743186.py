a, b, c, d = map(int, input().split())
al = set(range(a, b))
bo = set(range(c, d))
print(len(al & bo))