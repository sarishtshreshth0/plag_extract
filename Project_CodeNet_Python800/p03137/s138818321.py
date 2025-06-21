n,m=map(int,input().split())
x=list(map(int,input().split()))
x.sort()
xx=[]
for i in range(len(x)-1):
  if len(x)==1:
    xx.append(x[0])
    break
  s=x[i+1]-x[i]
  xx.append(s)
  
xx.sort(reverse=True)
ans=sum(xx[n-1:])
print(ans)
