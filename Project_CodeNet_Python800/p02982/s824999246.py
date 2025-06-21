n,d = list(map(int, input().split()))
X = [list(map(int, input().split())) for _ in range(n)]

def dist_squere(x, y):
    d = 0
    for i,j in zip(x,y):
        d += (i-j)**2
    return d

squares = set([i*i for i in range(10000)])
def is_square(x):
    return x in squares

from itertools import combinations

ans = 0
for x,y in combinations(X, 2):
    if is_square(dist_squere(x, y)):
        ans += 1

print(ans)