import numpy as np

N, D = map(int,input().split())
X = []
cnt = 0
for i in range(N):
    X.append(list(map(int,input().split())))

X = np.array(X)
for k in range(N):
    for l in range(k+1, N):
        Xd = X[k] - X[l]
        dis = np.linalg.norm(Xd, ord=2)

        if dis.is_integer():
            cnt += 1

print(cnt)