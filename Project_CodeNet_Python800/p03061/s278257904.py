from math import gcd

N=int(input())
A=list(map(int,input().split()))

if N==2:
    print(max(A))
else:
    L=[0 for _ in range(N)]
    R=[0 for _ in range(N)]
    L[0]=A[0]
    R[-1]=A[-1]
    for i in range(1,N):
        L[i]=gcd(A[i-1],L[i-1])
        R[N-1-i]=gcd(A[N-i],R[N-i])
    ans=max(L[-1],R[0])
    for j in range(1,N-1):
        ans=max(ans,gcd(L[j],R[j]))
    print(ans)