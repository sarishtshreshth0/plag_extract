from fractions import gcd

n=int(input())
A=list(map(int,input().split()))

L=[0]*n
R=[0]*n
L[0]=A[0]
R[n-1]=A[n-1]
res=0

for i in range(1,n):
	L[i]=gcd(L[i-1],A[i])
for i in range(0,n-1):
	R[n-i-2]=gcd(R[n-i-1],A[n-i-2])

for i in range(1,n-1):
	res=max(res,gcd(L[i-1],R[i+1]))
	
print(max(res,L[n-2],R[1]))