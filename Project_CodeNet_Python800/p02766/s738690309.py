n,k=map(int,input().split())
import math
a=math.log(n,k)
b=math.ceil(a)
if a==b:
    print(b+1)
else:
    print(b)