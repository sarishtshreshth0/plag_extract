[n, k] = [int(i) for i in input().split()]
for i in range(40):
    if n < k**i:
        print(i)
        break