check=[i*i for i in range(1000)]
n,d=list(map(int,input().split()))

def distance(x,y):
  num=0
  for i in range(d):
    num=num+(x[i]-y[i])*(x[i]-y[i])
  return num

diff=[]
for i in range(n):
  x=list(map(int,input().split()))
  diff.append(x)

ans=0
for i in range(n-1):
  for j in range(i+1,n):
    k=distance(diff[i],diff[j])
    if k in check:
      ans+=1
  
print(ans)
