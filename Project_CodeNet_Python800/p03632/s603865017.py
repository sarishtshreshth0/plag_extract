def resolve():
	a, b, c, d = map(int, input().split())
	if a > d or c > b:
		print(0)
		return
	print(min(b, d) - max(a, c))
resolve()