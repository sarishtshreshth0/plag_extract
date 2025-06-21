import math

n, x = map(int, input().split())
X = sorted(list(map(int, input().split())))
dis = [0] * (n-1)

xdis = 0
for i in range(n-1):
    dis[i] = X[i+1] - X[i]
    if X[i] <= x <= X[i+1]:
        xdis = min(abs(x-X[i]), abs(X[i+1]-x))

if n == 1:
    print(abs(X[0]-x))
    exit()
        
reg = xdis

for i in range(n-1):
    reg = math.gcd(reg, dis[i])

print(reg)