import math
n, d = map(int, input().split())
x = [list(map(int,input().split())) for i in range(n)]
count = 0

for i in range(n):
    for j in range(i+1, n):
        a = 0
        for k in range(d):
            a += pow(x[i][k]- x[j][k], 2)
            
        a = math.sqrt(a)
        b = int(a)
        if a == b:
            count += 1

print(count)