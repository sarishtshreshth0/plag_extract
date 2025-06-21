N=int(input())
a=list(map(int,input().split()))
dp=[0]*(10**5+3)
for i in range(N):
  for j in range(3):
    dp[a[i]+j]+=1
print(max(dp))