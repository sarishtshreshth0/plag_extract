S = input()
a, b = 0, 0
SS = '01'
for i in range(len(S)):
	if S[i] != SS[i % 2]:
		a += 1
	if S[i] != SS[1 - i % 2]:
		b += 1
print(min(a, b))
