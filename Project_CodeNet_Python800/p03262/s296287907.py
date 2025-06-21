import math
import functools
N,X = map(int,input().split())
A = list(map(int,input().split()))
mylist=[abs(X-A[0])]

for i in range(len(A)-1):
    mylist.append(abs(A[i+1]-A[i]))

print(functools.reduce(math.gcd, mylist))