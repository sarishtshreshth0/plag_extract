import math

n = int(input())
i = math.ceil(n ** 0.5)

while i > 0:
    if n % i == 0:
        print(len(str(n // i)))
        break
    i -= 1