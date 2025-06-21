import math
n = int(input())
ans = float('inf')
i = 1
while i <= math.sqrt(n):
    if n % i == 0:
        a = int(len(str(i)))
        b = int(len(str(n // i)))
        ans = min(ans,max(a,b))
    i += 1
print(ans)