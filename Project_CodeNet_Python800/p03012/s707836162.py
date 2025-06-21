N = int(input())
X = list(map(int,input().split()))
A = 10**10
R = sum(X)
K = 0
for i in range (N-1):
	K += X[i]
	R -= X[i]
	A = min(A, abs(K-R))
print(A)