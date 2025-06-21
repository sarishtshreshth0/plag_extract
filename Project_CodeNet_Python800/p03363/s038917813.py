import math
N = int(input())
A = list(map(int, input().split()))

if N == 1:
	if A[0] == 0:
		print(1)
		exit()
	else:
		print(0)
		exit()

count = 0

for i in range (1, N):
	A[i]+=A[i-1]

A = sorted(A)

if A[0] == 0:
	zeros = 1
else:
	zeros = 0

pittan = A[0]
countB = 1

for i in range (1, N):
	if A[i] == 0:
		zeros+=1
	if A[i] == A[i-1]:
		countB+=1
	else:
		count+=math.comb(countB, 2)
		countB = 1
		pittan = A[i]

print(count+zeros+math.comb(countB, 2))