def resolve():
	c = [i for i in range(2, 14)]
	c.append(1)
	a, b = map(int, input().split())
	if c.index(a) == c.index(b):
		print("Draw")
	elif c.index(a) > c.index(b):
		print("Alice")
	else:
		print("Bob")
resolve()