N = int(input())
S = list(input())
n = 1
for i in range(1, N):
	if S[i-1] != S[i]:
		n += 1
print(n)