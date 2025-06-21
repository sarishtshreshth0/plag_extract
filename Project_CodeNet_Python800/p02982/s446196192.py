import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n, d = inintm()

X = []
ans = 0

for _ in range(n):
    x = inintl()
    X.append(x)


for i in range(n):
    Xi = X[i]
    for j in range(i+1, n):
        Xj = X[j]
        z = 0
        for k in range(d):
            z += (Xi[k] - Xj[k])**2
        if z**0.5 == int(z**0.5):
            ans += 1

print(ans)
