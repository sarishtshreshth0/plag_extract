from collections import deque
N, M = map(int, input().split())
Clear = [-1]*N
T = [[] for _ in range(N)]
ans = 0
for i in range(M):
    X, Y, Z = map(int, input().split())
    X -= 1
    Y -= 1
    T[X].append(Y)
    T[Y].append(X)

for i in range(N):
    if Clear[i] == -1:
        ans += 1
        Clear[i] = 1
        P = deque([i])
        while(len(P) > 0):
            t = P.popleft()
            for j in T[t]:
                if Clear[j] == -1:
                    Clear[j] = 1
                    P.append(j)
print(ans)