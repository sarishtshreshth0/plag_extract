from math import gcd
#リスト l の最大公約数
def gcdlist(l):
    a = l[0]
    for i in range(len(l)):
        a = gcd(a,l[i])
    return a
n = int(input())
A = list(map(int, input().split()))
ans = 0

x = [0]*n
y = [0]*n
for i in range(1, n):
    x[i] = gcd(x[i-1], A[i-1])
for i in reversed(range(n-1)):
    y[i] = gcd(y[i+1], A[i+1])

for i in range(n):
    tmp = gcd(x[i], y[i])
    ans = max(ans, tmp)

print(ans)