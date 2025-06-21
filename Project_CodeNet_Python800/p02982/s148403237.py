import math

N, D = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(N)]
counter = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        temp = 0
        for k in range(D):
            temp += ((x[i][k] - x[j][k]) ** 2)
        temp = math.sqrt(temp)
        if temp.is_integer():
            counter += 1
print(counter)
