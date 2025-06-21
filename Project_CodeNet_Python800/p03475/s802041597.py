n = int(input())
train = [list(map(int, input().split())) for _ in range(n - 1)]

for i in range(n):
    cost = 0
    for j in range(i, n - 1):
        c, s, f = train[j]
        if cost >= s:
            cost += (s - cost) % f + c
        else:
            cost = c + s
    print(cost)