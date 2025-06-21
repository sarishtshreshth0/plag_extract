n=int(input())
A=list(map(int,input().split()))

R=[A[0]]*n
for i in range(n-1):
    R[i+1]=R[i]+A[i+1]

R=[0]+R
from collections import Counter
ans=0
for i in Counter(R).values():
    ans+= i*(i-1)//2
print(ans)