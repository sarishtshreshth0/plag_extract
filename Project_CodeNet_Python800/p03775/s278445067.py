import math

n = int(input())
i = [i for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0][-1]
print(len(str(max(i, n // i))))