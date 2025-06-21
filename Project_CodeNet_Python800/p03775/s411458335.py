from math import sqrt
n = int(input())
start = int(sqrt(n) // 1)
low_share = 0

for i in range(start,0,-1):
    if n % i == 0:
        low_share = i
        break

high_share = int(n/low_share)
ans = len(str(high_share))
print(ans)