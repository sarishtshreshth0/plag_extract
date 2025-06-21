N,K = map(int,input().split())
tmp = 1
for i in range(1,40):
    if N >= K**i:
        tmp = i+1
    else:
        print(tmp)
        break
