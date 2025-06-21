N = int(input())
P = [[0, 0, 0]for _ in range(2*N)]
for i in range(N):
    x, y = map(int, input().split())
    P[i] = [0, x, y]
for i in range(N):
    x, y = map(int, input().split())
    P[N+i] = [1, x, y]
P.sort(key=lambda x: x[1])
cnt = 0
for i in range(2*N):
    if P[i][0] == 0:
        continue
    else:
        if i == 0:
            continue
        else:
            M = [-1, -1]
            for j in range(i):
                if P[j][0] == 0:
                    if P[j][2] > M[1] and P[j][2] < P[i][2]:
                        M = [j, P[j][2]]
            if M[0] != -1:
                cnt += 1
                P[M[0]][0] = 2
print(cnt)
