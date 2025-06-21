import math

N = int(input())
ans = 100
sqrt = math.sqrt(N)
for i in range(1, math.floor(sqrt) + 1):
    if N % i == 0:
        temp = max(i, N // i)
        ans = min(ans, len(str(temp)))
print(ans)
