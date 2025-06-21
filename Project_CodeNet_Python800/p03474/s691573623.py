a,b = map(int, raw_input().split())
s = raw_input()
def f(s,a):
	for i,l in enumerate(s):
		if i != a and l not in map(str, range(10)): return False
	return True
print 'Yes' if s[a] == '-' and f(s,a) else 'No'