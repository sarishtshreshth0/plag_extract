N,K=map(int,input().split())
i=0
while True:
    if N<K**i:
        print(i)
        break
    i+=1