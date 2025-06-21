import math
N, D = map(int, input().split())
X = [list(map(int, input().split())) for i in range(N)]
num = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        A, B = X[i], X[j]
        d = math.sqrt(sum([(A[k] - B[k]) ** 2 for k in range(D)]))
        if abs(d - int(d)) < 10 ** (-4):
            num += 1
print(num)