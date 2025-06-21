import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
n = int(input())
a_ls = list(map(int, input().split()))
a_csum = [0] * n
now = 0
for i in range(n):
    now += a_ls[i]
    a_csum[i] = now
a_csum.append(0)
a_csum.sort()
ans = 0
now = 0
for i in range(n):
    if a_csum[i] == a_csum[i+1]:
        now += 1
    else:
        if now > 0:
            ans += combinations_count(now+1,2)
        now = 0
if now > 0:
    ans += combinations_count(now+1,2)
print(ans)
