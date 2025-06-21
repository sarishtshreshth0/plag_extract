import math

n = int(input())
ans = math.inf
for i in range(1, int(n ** 0.5) + 1):
    if (n / i).is_integer():
        ans = min(ans, max(len(str(i)), len(str(int(n / i)))))
print(ans)
