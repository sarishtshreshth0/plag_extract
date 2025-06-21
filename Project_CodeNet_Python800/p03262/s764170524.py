import sys
n,x=map(int,input().split())
xlist=[abs(x-int(y)) for y in input().split()]

def gcd(x,y):
    if x<y:
        x,y=y,x
    #x>y
    if y==0:
        return x
    if x%y==0:
        return y
    else:
        return gcd(y,x%y)

if n==1:
    print(xlist[0])
    sys.exit()

ans=0
for i in range(n-1):
    if i==0:
        ans=gcd(xlist[i],xlist[i+1])
    else:        
        ans=min(ans,gcd(xlist[i],xlist[i+1]))
print(ans) 