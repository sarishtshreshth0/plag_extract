n, m = map(int, input().split())
x = list(map(int, input().split()))
y = sorted(x)
keep = []
ans = 0
for i in range(m - 1):
    keep.append(y[i + 1] - y[i])
keep = sorted(keep)
for i in range(max(0, m - n)):
    ans += keep[i]
print(ans)
