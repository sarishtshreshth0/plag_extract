import math

# 最大公約数を求める問題
N, X = map(int, input().split())
x = [int(_) for _ in input().split()]
if N == 1:
    print(abs(x[0]-X))
    exit()

x.sort()
# N > 1と仮定
for i in range(N-1):
    if x[i] < X and x[i+1] > X:
        x = x[:i+1] + [X] + x[i+1:]
        break
    elif x[i] >= X:
        x = [X] + x
        break
    elif x[i+1] <= X:
        x = x + [X]
        break

if len(x) >= 3:
    base = math.gcd(x[1]-x[0], x[2]-x[1])
    for i in range(2, N):
        diff = x[i+1] - x[i]
        base = math.gcd(base, diff)
    print(base)
else:
    print(x[1] - x[0])
