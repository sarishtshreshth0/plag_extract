N=int(input())
a=list(map(int,input().split()))

d = [0]*(10**5+1)
for i in range(N):
  d[a[i]]+=1

ans=0
for i in range(10**5):
  ans = max(ans, d[i-1]+d[i]+d[i+1])

print(ans)