N,K=map(int,input().split())
cnt=0
while N>=K:
    cnt+=1
    N//=K
print(cnt+1)