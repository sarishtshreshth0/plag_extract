import math

N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

for i in range(N - 1):
    for j in range(i + 1, N):
        tmp = 0
        for k in range(D):
            tmp += ((X[i][k] - X[j][k])** 2)
        tmp = math.sqrt(tmp)
        if tmp.is_integer():
            cnt += 1

print(cnt)
