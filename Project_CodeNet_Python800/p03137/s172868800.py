n, m = map(int, input().split())
if n >= m:
    print(0)
else:
    x = [int(i) for i in input().split()]
    x.sort()
    d = x[- 1] - x[0]
    y = []
    for i in range(m - 1):
        y.append(x[i + 1] - x[i])
    y.sort(reverse=True)
    for i in range(n - 1):
        d -= y[i]
    print(d)