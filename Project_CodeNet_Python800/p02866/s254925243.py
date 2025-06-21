import collections
n=int(input())
a=list(map(int,input().split()))
if a[0]==0 and a.count(0)==1:
  ans=1
else:
  ans=0
a=collections.Counter(a)
for i in range(max(a)):
  ans*=a[i]**a[i+1]
  ans%=998244353
print(ans)