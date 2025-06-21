n = int(input())
a = list(map(int, input().split()))
mod = 998244353
if a[0]!=0:
  print(0)
  quit()
#a.sort()
l=max(a)+1
dp1 = [0]*l
dp2 = [0]*l
ans=0
for i in a:
  dp1[i]+=1
#print(dp1)  

if dp1[0]!=1:
  print(0)
  quit()

dp2[0]=1
#print(dp2)
for i in range(1, l):
  dp2[i]=dp2[i-1]*(dp1[i-1]**dp1[i])
  dp2[i]%=mod

#print(dp2)
print(dp2[l-1])