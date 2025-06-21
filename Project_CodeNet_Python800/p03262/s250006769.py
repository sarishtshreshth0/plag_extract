import sys
import math


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n, x = inintm()
X = inintl()

if x not in X:
    X.append(x)
    n += 1

X.sort()

ans = X[1] - X[0]
prev = X[0]

for i in range(1,n):
    ans = min(math.gcd(ans, X[i]-prev), ans)
    prev = X[i]

print(ans)
