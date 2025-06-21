from collections import Counter
n,*a=map(int,open(0).read().split())
for i in range(1,n):
  a[i]=a[i-1]+a[i]
ans=0
for _,k in Counter([0]+a).items():
  ans+=k*(k-1)//2
print(ans)