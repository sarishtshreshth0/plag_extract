def getlist():
	return list(map(int, input().split()))

X = getlist()
Y = sorted(X)
if X[2] == Y[1]:
	print("Yes")
else:
	print("No")