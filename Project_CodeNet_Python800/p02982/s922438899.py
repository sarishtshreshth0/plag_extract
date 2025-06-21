import math
n, d = map(int, input().split())

x = []
for _ in range(n):
    x.append(list(map(int, input().split())))

count = 0
for i in range(n):
    for j in range(i+1, n):
        s = 0
        for k in range(d):
            diff = x[i][k]-x[j][k]
            s += diff * diff
        sq = math.sqrt(s) 
        if sq == int(sq):
            count += 1
print(count)
