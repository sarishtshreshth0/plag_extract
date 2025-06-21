import math
import itertools

N, D = [int(n) for n in input().split()]
X = []
for i in range(N):
    X.append([int(m) for m in input().split()])

def get_distance(p1, p2):
    d2 = 0
    for i in range(D):
        d2 += (p1[i] - p2[i])**2
    return math.sqrt(d2)

count = 0
for i, j in itertools.combinations(range(N), 2):
    if get_distance(X[i], X[j]).is_integer():
        count += 1

print(count)