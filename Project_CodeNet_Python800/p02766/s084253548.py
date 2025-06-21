N,K = map(int,input().split())
ans=1
p=K
while p <= N:
  p *= K
  ans+=1
print(ans)