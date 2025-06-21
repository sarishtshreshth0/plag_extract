n = int(input())
maps = []
for i in range(n-1):
    maps.append(list(map(int, input().split())))

import math
result = []
for i, item in enumerate(maps):
    cost = item[0] + item[1]
    for j in range(i+1, n-1):
        next_cost = maps[j][1]
        if cost <= next_cost:
            cost = next_cost + maps[j][0]
        else:
            gap = cost - next_cost
            gap = math.ceil(gap/maps[j][2])
            cost = next_cost + maps[j][2]*gap + maps[j][0]
    result.append(cost)

for i in result:
    print(i , flush=True)
print(0 , flush=True)
