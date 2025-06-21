n, m = map(int, input().split())
x = list(map(int, input().split()))

x.sort()
x_diff = []
for i in range(m-1):
    x_diff.append(x[i+1] - x[i])

x_diff.sort()

ans = 0
for i in range(len(x_diff) - (n-1)):
    ans += x_diff[i]
print(ans)