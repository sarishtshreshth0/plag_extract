n,k = map(int, input().split())

for i in range(1000000):
    if k**i > n:
        print(i)
        break