def qsimulator(s, a, b):
	paas = 0
	bpaas = 0
	aflg = True
	bflg = True
	total = a + b
	res = []
	for i in s:
		if i == 'c':
			res.append("No")
		elif i == 'a':
			if aflg and paas < total:
				paas += 1
				res.append("Yes")
			else:
				aflg = False
				res.append("No")
		else:
			if bflg and paas < total and bpaas < b:
				paas += 1
				bpaas += 1
				res.append("Yes")
			else:
				bflg = False
				res.append("No")
	return res
n, a, b = map(int, input().split())
s = input()
ans = qsimulator(s, a, b)
for i in ans:
	print(i)