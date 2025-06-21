N, K = map(int, input().split())
for i in range(1000000):
    if K ** (i - 1) <= N < K ** i:
        print(i)
        break
