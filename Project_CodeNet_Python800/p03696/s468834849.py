n, s = int(raw_input()), raw_input()
h = {'(':+1 , ')':-1}
m = 0
bal = 0
for i in range(len(s)):
	bal += h[s[i]]
	m = min(bal,m)

print '(' *abs(m) + s + ')' * (bal + abs(m))