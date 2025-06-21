n = int(raw_input())
m = len(str(n))
for a in range(2, int(n ** 0.5) + 1):
	if n % a == 0:
		m = min(m, max(len(str(a)), len(str(n/a))))
print m