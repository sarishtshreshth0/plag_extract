from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))
s=[0]*(n+1)
for i in range(n):s[i+1]=s[i]+a[i]
d=defaultdict(int)
for i in range(n+1):d[s[i]]+=1
r=0
for v in d.values():
  r+=int(v*(v-1)/2)
print(r)