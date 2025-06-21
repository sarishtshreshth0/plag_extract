n = int(input())
s = list(input())
slime = []
for i in range(n-1):
	if s[i] != s[i+1]:
		slime.append(s[i+1])
print(len(slime)+1)