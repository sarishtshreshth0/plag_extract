N,X=map(int,input().strip().split())
x=list(map(int,input().strip().split()))
x.append(X)
x.sort()
    
d=[]
for n in range(1,N+1):
    d.append(x[n]-x[n-1])
    
def gcd(a,b):
    x=max(a,b)
    y=min(a,b)
    tmp=x%y
    if tmp==0:
        return y
    else:
        return gcd(y,tmp)
    
if len(d)<=1:
    print(d[0])
else:
    D=d[0]
    for i in range(1,len(d)):
        D=gcd(D,d[i])
    print(D)