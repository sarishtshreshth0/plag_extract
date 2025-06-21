n=int(input())
w=list(map(int,input().split()))
ans=float('inf')
for i in range(1,len(w)):
  sabun=abs(sum(w[:i])-sum(w[i:]))
  ans=min(ans,sabun)
print(ans)