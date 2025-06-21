def prefix_XOR(n):
	if n&1:
		if n&2:
			return 0
		else:
			return 1
	else:
		return (n+1)^prefix_XOR(n+1)
A, B = map(int,input().split())
print(prefix_XOR(B)^prefix_XOR(A-1))