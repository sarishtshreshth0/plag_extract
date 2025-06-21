import math
N = int(input())
sqrt = math.floor(math.sqrt(N))
ans = 10
for A in range(1,sqrt+1):
    n = 0
    if N % A != 0:
        continue
    B = N / A
    while not B == 0:
        n += 1
        B //= 10
    ans = min(ans, n)
print(ans)
