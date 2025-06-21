from math import gcd
n = int(input())
A = list(map(int, input().split()))
L = [0]
for i in range(n):
    L.append(gcd(L[-1], A[i]))
R = [0]
for i in range(n):
    R.append(gcd(R[-1], A[-i-1]))
R = R[::-1]
ans = 0
for i in range(n):
    ans = max(ans, gcd(L[i],R[i+1]))
print(ans)