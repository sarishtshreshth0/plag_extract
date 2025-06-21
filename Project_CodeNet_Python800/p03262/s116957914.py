import math

n, s = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in a:
    ans = math.gcd(ans, abs(i - s))
print(ans)
