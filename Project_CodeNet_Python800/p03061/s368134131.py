import math

N = int(input())
A = list(map(int, input().split()))

gcd_l = [0]
gcd_r = [0]

for n in range(N):
    gcd_l.append(math.gcd(gcd_l[n], A[n]))
    gcd_r.append(math.gcd(gcd_r[n], A[-(n + 1)]))
#print(gcd_r)
#print(gcd_l)

gcd_r = gcd_r[::-1]
#print(gcd_r)

ans = []
for n in range(N):
    ans.append(math.gcd(gcd_l[n], gcd_r[n + 1]))
print(max(ans))
#print(ans)
