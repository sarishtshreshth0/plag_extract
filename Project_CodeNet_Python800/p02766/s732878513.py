N,K=map(int,input().split())
for i in range(10**18):
    if K**i<=N<K**(i+1):
        print(i+1)
        break