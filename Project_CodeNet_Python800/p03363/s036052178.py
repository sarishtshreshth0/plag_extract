n=int(input())
a=[0] + list(map(int,input().split()))

from collections import defaultdict
dic=defaultdict(int)
dic[0]=1
for i in range(n):
  a[i+1]=a[i+1]+a[i]
  dic[a[i+1]]+=1
  
ans=0
for val in dic.values():
  ans+=(val*(val-1))//2
print(ans)