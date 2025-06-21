import math

n = int(input())
l = [i for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0]
print(len(str(max(l[-1], n // l[-1]))))