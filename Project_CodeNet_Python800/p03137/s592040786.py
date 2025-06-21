n, m = map(int, input().split())
x = list(map(int, input().split()))

dis = []
if m <= n:
    print(0)
else:
    x.sort()
    for i in range(m - 1):
        dis.append(abs(x[i] - x[i + 1]))
    dis.sort()
    sum(dis[- n + 1:])
    print(sum(dis[:m - n]))
