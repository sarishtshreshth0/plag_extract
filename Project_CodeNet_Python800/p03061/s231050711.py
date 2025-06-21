import math

n = int(input())
a = [int(xi) for xi in input().split()]

L=[a[0]]
gcdl = a[0]
R=[a[n-1]]
gcdr = a[n-1]
for xi in range(1,n):
    gcdl = math.gcd(gcdl,a[xi])
    L.append(gcdl)

for xi in range(n-2,-1,-1):
    gcdr = math.gcd(gcdr,a[xi])
    R.append(gcdr)

R.reverse()

# print("R", R)
# print("L", L)
m = []
m.append(R[1])
m.append(L[n-2])
# print(m)

if n>2:
    for xi in range(1,n-1):
        m.append(math.gcd(L[xi-1],R[xi+1]))
        # print(xi, R[xi+1],L[xi-1])

# print(m)
print(max(m))
