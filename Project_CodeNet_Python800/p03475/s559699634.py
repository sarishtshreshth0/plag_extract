import math

N = int(input())
lines = [list(map(int, input().split())) for i in range(N-1)]

cost = []

for i in range(N):
    time = 0
    for j in range(i, N-1):
        C, S, F = lines[j]
        if time < S:
            time = S + C
        else:
            time = F*math.ceil(time/F) + C
    cost.append(time)

for c in cost:
    print(c)


