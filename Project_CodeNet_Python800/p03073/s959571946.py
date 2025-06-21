S = list(input())
n = len(S)
for j in range(n):
	S[j] = int(S[j])
cnt = 0
for i in range(n-1):
	if S[i] == S[i+1]:
		S[i+1] = abs(S[i]-1)
		cnt += 1
print(cnt)