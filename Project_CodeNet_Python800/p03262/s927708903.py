def gcd(a, b):
    if a == b: return a
    while b > 0: a, b = b, a % b
    return a

n,x=(int(i) for i in input().strip().split(" "))
from functools import reduce
ar=[int(i) for i in input().strip().split(" ")]
ar.sort()
from bisect import insort
insort(ar,x)
temp=[]
for i in range(1,len(ar)):
    temp.append(abs(ar[i]-ar[i-1]))

k=reduce(gcd,temp)
print(k)