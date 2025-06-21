import math
n,d = map(int,input().split())
a = [list(map(int, input().split())) for i in range(n)]
count = 0

for i in range(n-1):
    for j in range(i+1, n):
        dis = 0
        for k in range(d):
            dis += (a[i][k] - a[j][k])**2
        if math.sqrt(dis) == int(math.sqrt(dis)):
            count += 1
print(count)
