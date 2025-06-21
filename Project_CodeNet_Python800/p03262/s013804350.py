import math
N,X = map(int,input().split())
xs = list(map(int,input().split()))
diffs = []
g = abs(X- xs[0])
for i in range(1,N):
    g = math.gcd(g,abs(X-xs[i]))
print(g)
