a, b, c, d = map(int, input().split())
al = [x for x in range(a,b)]
cl = [y for y in range(c,d)]

print(len(al+cl)-len(set(al+cl)))