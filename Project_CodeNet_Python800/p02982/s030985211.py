from itertools import combinations
N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
data = [0]*16002
i = 1
while i**2<=16001:
    data[i**2]=1
    i += 1
res = 0
for a, b in combinations(X,2):
    temp = 0
    for x, y in zip(a, b):
        temp += (x-y)**2
    if data[temp]:
        res += 1
print(res)