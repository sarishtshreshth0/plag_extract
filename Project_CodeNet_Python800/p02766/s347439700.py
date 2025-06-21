N, K = (int(x) for x in input().split())
ans=0
while(N>=1):
  N = int(N/K)
  ans+=1

print(ans)