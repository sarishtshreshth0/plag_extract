N, D = map(int,input().split())

X = []
ans = 0
for i in range(N):
    X.append(list(map(int,input().split())))

    for j in range(i):
        dis = 0
        for k in range(D):
            dis += (X[i][k] - X[j][k])**2
            if k == D-1:
                if (dis) ** (1/2) - int((dis) ** (1/2)) == 0:
                    ans += 1

print(ans)