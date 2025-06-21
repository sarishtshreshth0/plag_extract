def bishop(n, m):
	if n == 1 or m == 1:
		return 1
	if n % 2 == 0:
		return (n // 2) * m
	else:
		return (((n // 2)+1) * m) - (m // 2)
n, m = map(int, input().split())
print(bishop(n, m))