n,k = map(int, input().split())
for i in range(32):
    if k**i <= n < k**(i+1):
        print(i+1)
        break