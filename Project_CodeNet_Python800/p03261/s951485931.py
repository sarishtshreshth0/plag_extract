import sys
N = int(input())
S = [input() for s in range(N)]
s = set(S)
if len(S) != len(s):
	print("No")
	sys.exit()
for i in range(N-1):
	if S[i][-1] != S[i+1][0]:
		print("No")
		sys.exit()
print("Yes")