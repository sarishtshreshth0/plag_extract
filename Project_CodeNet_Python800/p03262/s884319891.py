import math
n, x = [int(w) for w in input().split()]
la = [int(w) for w in input().split()]+[x]
la.sort()
if la[0] < 0:
    m = la[0]
    la = [w+m for w in la]

diff = [0]*n
for i in range(n):
    diff[i] = la[i+1]-la[i]
g = diff[0]
for i in diff[1:]:
    g = math.gcd(g, i)

print(g)
