n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
k=abs(a[-1]-a[0])
b=[]
for i in range(m-1):
  b.append(abs(a[i+1]-a[i]))
b.sort()
if n==1:
  print(k)
else:
  print(k-sum(b[-n+1:]))