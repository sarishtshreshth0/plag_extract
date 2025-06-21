import math
N,D = map(int,input().split())
counter = 0
X = []
for i in range(N):
    ls = list(map(int,input().split()))
    X.append(ls)
for i in range(N-1):
    for j in range(i+1, N):
        dist = 0
        for k in range(D):
            dist += (X[i][k] - X[j][k])**2
        for l in range(1,int(math.sqrt(dist))+1):
            if l**2 == dist:
                counter += 1
print(counter)