import math

N, X = map(int, input().split())
x = sorted(list(map(int, input().split())) + [X])
X = -x[0] + x[1]
for i in range(N):
    X = math.gcd(X, x[i] - x[i + 1])
print(X)
