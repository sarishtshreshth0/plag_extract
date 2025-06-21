n, k = map(int, input().split())

for i in range(1, 10**4):
    if n < k**i:
        print(i)
        exit()