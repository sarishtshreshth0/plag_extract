n,x=map(int,input().split())
a=list(map(int,input().split()))
b=[]
if n==1 and x==a[0]:
    print(max(x,10**9-x))
    exit()
for i in range(n):
    b.append(abs(a[i]-x))
import math
c=0
for i in range(n):
    c=math.gcd(c,b[i])
    if c==1:
        break
print(c)