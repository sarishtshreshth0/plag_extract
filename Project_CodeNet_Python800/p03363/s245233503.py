N=int(input())
*A,=map(int,input().split())

S=[0]+A
for i in range(1,N+1):
    S[i]=S[i]+S[i-1]

from collections import*
C=Counter(S)
ans=0
for v in C.values():
    ans+=v*(v-1)//2

print(ans)