n = int(input())
train = [list(map(int, input().split())) for _ in range(n-1)]

for i in range(n):
    t = 0
    for j in range(i, n-1):
        c, s, f = train[j]
        t = max(t, s)
        t += (f - t % f) % f
        t += c
    print(t)