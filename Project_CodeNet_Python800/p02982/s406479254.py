# -*- coding: utf-8 -*-
import math

def get_dist(x, y, d):
    dist = 0
    for i in range(d):
        dist += (x[i] - y[i]) ** 2

    return math.sqrt(dist)


N, D = map(int, input().split())
X_list = []
for i in range(N):
    X_list.append(list(map(int, input().split())))

cnt = 0
for i in range(N):
    for j in range(i+1, N, 1):
        x = X_list[i]
        y = X_list[j]
        num = get_dist(x, y, D)
        if(num.is_integer()):
            cnt += 1

print(cnt)
