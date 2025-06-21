n, m = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
dx = [0] * (m - 1)
for i in range(m - 1):
    dx[i] = x[i + 1] - x[i]
dx.sort()
print(sum(dx[:m-n]) if m > n else 0)