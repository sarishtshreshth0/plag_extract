n,k = map(int,input().split())
for i in range(100000):
  if k**(i-1) <= n < k**i:
    print(i)
    break