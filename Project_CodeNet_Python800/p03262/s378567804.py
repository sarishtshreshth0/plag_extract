N,X=map(int,input().split())
C=list(map(int,input().split()))

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

A=[0]*N
for i in range(N):
    A[i]=abs(C[i]-X)

ans=A[0]
for i in range(1,N):
    ans=gcd(ans,A[i])

print(ans)