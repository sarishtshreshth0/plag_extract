import math
from functools import reduce
def gcd_list(numbers):
    return reduce(math.gcd, numbers)
a,b=map(int,input().split())
c=list(map(int,input().split()))
d=[]
for i in c:
    d.append(abs(b-i))
print(gcd_list(d))