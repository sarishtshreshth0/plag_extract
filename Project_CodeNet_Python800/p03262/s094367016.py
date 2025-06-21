import fractions
from functools import reduce
n,s=map(int,input().split())
x=list(map(int,input().split()))
#print(x)

for i in range(n):
    x[i]=abs(x[i]-s)

print(reduce(fractions.gcd,x))
