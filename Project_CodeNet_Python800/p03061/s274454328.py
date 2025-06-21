from math import gcd

N=int(input())
A=list(map(int,input().split()))

if N==2:
    print(max(A))
else:
    r1=max(gcd(A[0],A[1]),gcd(A[1],A[2]),gcd(A[2],A[0]))
    a=gcd(A[2],gcd(A[0],A[1]))

    for i in range(3,N):
        r1=max(gcd(A[i],r1),a)
        a=gcd(a,A[i])
    print(r1)