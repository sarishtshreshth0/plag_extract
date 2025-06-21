import math
n = int(input())
max_target = int(math.sqrt(n) // 1)
ans = 10 ** 9
for a in range(1, max_target + 1):
  if n % a == 0:
    b = n // a
    f = max(len(str(a)), len(str(b)))
    ans = min(ans, f)
print(ans)