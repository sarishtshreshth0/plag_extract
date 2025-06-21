n, m = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
y = []
for s, t in zip(x, x[1:]):
    y.append(t - s)
y.sort()
if n >= m:
    print(0)
else:
    print(sum(y[:-(n-m)]))
