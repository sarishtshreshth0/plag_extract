import math


N, D = map(int, input().split())
X = []
for i in range(N):
    X.append(list(map(int, input().split())))

count = 0
for i in range(N):
    for j in range(i+1, N):
        dist = 0
        for d in range(D):
            dist += (X[i][d] - X[j][d]) ** 2
        if float.is_integer(math.sqrt(dist)) == True:
            count += 1
            
print(count)