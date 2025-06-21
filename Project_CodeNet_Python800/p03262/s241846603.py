def A(a,b):
    if a<b:
        tmp = a
        a = b
        b = tmp
    r = a % b
    while r!=0:
      a = b
      b = r
      r = a % b
    return b
n,X=map(int,input().split())
x=list(map(int,input().split()))
x.append(X)
x.sort()
x2=[]
for i in range(1,n+1):
    x2.append(x[i]-x[i-1])
if len(x2)==1:
    p=x2[0]
else:
    for i in range(n):
        if i==0:
            p=A(x2[i-1],x2[i])
        elif i!=1:
            p=A(p,x2[i])
print(p)

