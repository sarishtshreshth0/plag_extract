#B - Good Distance
import math
N,D = map(int,input().split())
X = []
for _ in range(N):
    Xi = list(map(int,input().split()))
    X.append(Xi)
count = 0
for i in range(N):
    for k in range(i+1,N):
        D_sqrt = 0
        for j in range(D):
            D_sqrt += (X[i][j] - X[k][j])**2
        D_ans = math.sqrt(D_sqrt)
        if D_ans.is_integer():#float型が整数か判定するメソッド
            count += 1
print(count)