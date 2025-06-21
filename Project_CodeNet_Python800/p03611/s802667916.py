import collections

n=int(input())
a=list(map(int,input().split()))

b=[]
for i in range(n):
  c=a[i]
  d=a[i]-1
  e=a[i]+1
  b.append(c)
  b.append(d)
  b.append(e)
  
f=collections.Counter(b)

g=f.most_common()
print(g[0][1])