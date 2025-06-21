n = int(input())
w = list(map(int, input().split()))
res = 10 ** 9 + 7
for t in range(n - 1):
    u = sum(w[:t + 1])
    l = sum(w[t + 1:])
    dif = abs(u - l)
    if dif < res:
        res = dif
print(res)
