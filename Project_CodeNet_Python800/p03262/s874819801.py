N,X=map(int,input().split())
x=list(map(int,input().split()))
def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)
X=abs(X-x[0])
for i in range(N-1):
  X=gcd(max(X,abs(x[i+1]-x[i])),min(X,abs(x[i+1]-x[i])))
print(X)