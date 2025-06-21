import math

def get_distance(l1, l2):
    dis = 0
    for i in range(len(l1)):
        dis += (l1[i]-l2[i]) ** 2
    return math.sqrt(dis)

N, D = map(int, input().split())
X = []
ans = 0
for _ in range(N):
    X.append(list(map(int, input().split())))

for n in range(N-1):
    for d in range(n+1, N):
        dis = get_distance(X[n], X[d])
        if dis.is_integer():
            ans += 1

print(ans)
