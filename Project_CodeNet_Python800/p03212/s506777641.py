import collections

L = [3,5,7]
Q = collections.deque(L)
A = []


for i in range (0, 40000):
	V = Q.popleft()
	A.append(V)
	Q.append(V*10+3)
	Q.append(V*10+5)
	Q.append(V*10+7)

import bisect

D = []

for i in range (0, 40000):
	V = str(A[i])
	if V.count('3') > 0 and V.count('5') > 0 and V.count('7') > 0:
		D.append(int(V))

N = int(input())
print(bisect.bisect_right(D, N))