N,K = map(int,input().split())
for i in range(N):
    if N >=K**i and N <K**(i+1):
        print(i+1)
        break