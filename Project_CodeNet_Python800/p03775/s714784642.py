import math
N = int(input())
INF = float("inf")
for a in range(1, int(math.sqrt(N)) + 1):
    if N % a != 0:
        continue
    b = int(N / a)
    a = list(map(int, str(a)))
    b = list(map(int, str(b)))
    length = max(len(a), len(b))
    if INF > length:
        INF = length
print(INF)
