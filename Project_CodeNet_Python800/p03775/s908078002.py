import math

n = int(input())
l = []
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        a = len(str(int(n / i)))
        b = len(str(int(i)))
        l.append(max(a, b))

print(min(l))