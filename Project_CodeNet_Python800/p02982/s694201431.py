import math
N,D = map(int,input().split())
X = []
c = 0
s = 0
for i in range(N):
    X.append(list(map(int,input().split()))) 
for l in range(N):
    # print(str(l) + "l")
    if l == N - 1:
        break
    for i in range(l+1,N):
        for j in range(D):
            s += abs(X[l][j] - X[i][j]) ** 2
        s = math.sqrt(s)
        if s % 1 == 0:
            c += 1
        # print(str(i) + "i")
        s = 0

print(c)


