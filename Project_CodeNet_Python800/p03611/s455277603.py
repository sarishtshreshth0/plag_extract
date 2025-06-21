from collections import Counter

n=int(input())
a=list(map(int,input().split()))
a_max=max(a)

c=Counter(a)

ans=0
for i in range(a_max+1):
  ans=max(ans,c[i]+c[i+1]+c[i+2])

print(ans)