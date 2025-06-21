n, m = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
xd = [x[i] - x[i - 1] for i in range(1, m)]
xd.sort(reverse = True)
print(sum(xd[n - 1:]))