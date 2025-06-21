#ABC109-C
import math
from functools import reduce
def gcd(*numbers):
    return reduce(math.gcd,numbers)

n,X = map(int,input().split())
x = list(map(int,input().split())) 

x.append(X)
x.sort()

kosa = []

for i in range(1,n+1):
    k = (x[i]-x[i-1])
    kosa.append(k)
    
print(gcd(*kosa))