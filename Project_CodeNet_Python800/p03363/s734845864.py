import collections
N=int(input())
A=list(map(int,input().split()))

B=[0]
for i in range(1,N+1):
    B.append(A[i-1]+B[i-1])

b=collections.Counter(B)
ans=0
for key in b:
    n=b[key]
    ans+=n*(n-1)/2

print(int(ans))