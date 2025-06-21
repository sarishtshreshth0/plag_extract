import sys

N = int(input())
W = list(input() for _ in range(N))

if len(set(W)) == N:
	for i in range(N-1):
		a = W[i]
		b = W[i+1] 
		if a[-1] != b[0]:
			print('No')
			sys.exit()
	print('Yes')
else:
	print('No')