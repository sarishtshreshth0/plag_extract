from math import sqrt


def calc_distance(Y, Z):
    return sqrt(sum((y - z) ** 2 for y, z in zip(Y, Z)))


N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        distance = calc_distance(X[i], X[j])
        cnt += distance.is_integer()
print(cnt)