import math

n = int(input())

m = n

for i in range(1, math.floor(n ** 0.5) + 1):
    if n % i == 0:
        l = len(str(i))
        ll = len(str(n // i)) 
        if m > max(l, ll):
            m = max(l, ll)

print(m)