N=int(input())
from math import*
count=round(sqrt(N))+1
while count:
    if N%count==0:
        A=len(str(count))
        B=len(str(N//count))
        break
    else:
        count-=1
print(max(A,B))