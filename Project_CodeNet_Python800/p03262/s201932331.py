import math
from functools import reduce
N,X=map(int, input().split()) 
x = list(map(int, input().split()))
y=[0]*N
for i in range(N):
    y[i]=abs(x[i]-X)
def gcd(*numbers):
    return reduce(math.gcd, numbers)

def gcd_list(numbers):
    return reduce(math.gcd, numbers)
D=y[0]
for i in range(N):
    D=gcd(y[i],D)        
print(D)