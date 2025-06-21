N=int(input())
W=list(map(int,input().split()))


total=sum(W)
ans=10**10

for i in range(N):
    ans=min(ans,abs(2*sum(W[0:i])-total))
    
print(ans)

