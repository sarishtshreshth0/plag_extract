N,K=map(int,input().split())
X=0
i=0
while X<N:
    X=X+(K-1)*K**i
    i=i+1
print(i)