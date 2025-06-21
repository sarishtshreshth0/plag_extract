# coding: utf-8
import math
N = int(input())


saisho = 10**10
for i in range(1, int(math.sqrt(N)) + 1):
    if N % i == 0:
        fab = max(len(str(i)), len(str(N // i)))
        saisho = min(saisho, fab)

print(saisho)