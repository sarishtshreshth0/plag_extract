import itertools
import math

n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in itertools.combinations(x, 2):
    length = 0
    for j in range(d):
        length += (i[0][j] - i[1][j]) ** 2
    if math.sqrt(length) % 1 == 0:
        ans += 1
print(ans)
