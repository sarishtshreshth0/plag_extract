import math

N, X = map(int, input().split())
X_lst = list(map(int, input().split()))

if len(X_lst) == 1:
    print(abs(X_lst[0] - X))
    exit()

u = 0
if X_lst[0] == X:
    u = float('inf')

for i, x in enumerate(X_lst[1:], start=1):
    if x == X:
        u = float('inf')

    if X_lst[i - 1] < X < x:
        u = [X - X_lst[-1], x - X]

    if i == 1:
        g = X_lst[1] - X_lst[0]
    else:
        g = math.gcd(g, x - X_lst[i - 1])


if u == 0:
    u = [X - X_lst[-1]]
elif u != float('inf'):
    g = max(math.gcd(g, u[0]), math.gcd(g, u[1]))

print(g)
