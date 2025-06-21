import collections

mod=998244353
n=int(input())
arr=list(map(int,input().split()))
if arr[0]!=0:
  print(0)
else:
  count=collections.Counter(arr)
  if count[0]!=1:
    print(0)
  else:
    ans=1
    for i in range(1,n):
      ans*=pow(count[i-1],count[i],mod)
      ans%=mod
    print(ans)