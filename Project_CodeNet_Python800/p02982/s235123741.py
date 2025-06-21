import math
N,D = map(int, input().split())
X = [list(map(int, input().split())) for i in range(N)]
ans = 0
for i in range(N-1):
    for j in range(i+1,N):
        s = 0
        for k in range(D):
            s += (X[i][k] - X[j][k])**2
        if math.sqrt(s).is_integer():
            ans +=1
print(ans)