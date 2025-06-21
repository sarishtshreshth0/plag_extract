import fractions

N=int(input())
A=list(map(int,input().split()))

L=[0]*(N+1)
R=[0]*(N+1)

def gcd(x,y):
    if x==0 or y==0:
        return max(x,y)
    return fractions.gcd(x,y)

for i in range(N):
    j=N-i

    L[i+1]=gcd(L[i],A[i])
    R[j-1]=gcd(R[j],A[j-1])
ans=0

for i in range(N):
    ans=max(ans,gcd(L[i],R[i+1]))

print(ans)