import math
n = int(input())
a = 1
b = n

for i in range(1, int(math.sqrt(n))+1):
	if n % i == 0:
		a = i
		b = n // i
print(len(str(b)))