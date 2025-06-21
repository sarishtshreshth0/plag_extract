import math

N = int(input())

def digit(n):
    d = 0
    while n > 0:
        d += 1
        n //= 10

    return d

F = digit(N)

for n in range(1, int(math.sqrt(N)) + 1):
    if N % n != 0:
        continue
    else: # N % n == 0
        F = min(F, max(digit(n), digit(N // n)))

print(F)