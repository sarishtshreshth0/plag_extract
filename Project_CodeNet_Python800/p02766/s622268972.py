import math
N, K = map(int, input().split())

a = N
i = 1
while a >= K:
    a = a/K
    i += 1
print(i)

