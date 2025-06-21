A, B = map(int, input().split())

ones = [0] * 101
def calcones(end, pow):
	start = pow // 2
	if end < pow // 2:
		return 0
	
	n = (end - start + 1) // pow
	n *= pow // 2
	
	if 0 < (end - start + 1) % pow <= pow // 2:
		n += (end - start + 1) % pow
		
	return n

pow = 2
for i in range(1, 101):
	ones[i] = calcones(B, pow) - calcones(A-1, pow)
	pow *= 2
	
# print(ones)
		
ans = 0
pow = 1
for i in range(1, 101):
	ans += (ones[i] % 2) * pow
	pow *= 2
	
print(ans)