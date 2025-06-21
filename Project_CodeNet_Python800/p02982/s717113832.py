import math

N,D = map(int,input().split())
X = [list(map(int,input().split())) for _ in range(N)]

ans = 0

for i in range(N):
    for j in range(i+1,N):
        dist = 0
        for p in range(D):
            dist += (X[i][p]-X[j][p])*(X[i][p]-X[j][p])
        dist = math.sqrt(dist)
        if dist == int(dist):
            ans+=1
                
print(ans)