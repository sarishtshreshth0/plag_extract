
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

Ns = len(S)
Nt = len(T)

dp = [[0]*(Nt+1) for _ in range(Ns+1)]
path = [[None for _ in range(Nt+1)] for _ in range(Ns+1)]

for i in range(Ns):
    for j in range(Nt):
        if S[i]==T[j]:
            if dp[i+1][j+1] < dp[i][j]+1:
                dp[i+1][j+1] = dp[i][j]+1
                path[i+1][j+1] = (i,j)
        else:
            if dp[i][j+1] < dp[i+1][j]:
                dp[i+1][j+1] = dp[i+1][j]
                path[i+1][j+1] = (i+1,j)
            else:
                dp[i+1][j+1] = dp[i][j+1]
                path[i+1][j+1] = (i,j+1)


ans = []
cur = [Ns, Nt]
while cur[0] != 0 and cur[1] != 0:
    nxt = path[cur[0]][cur[1]]
    if cur[0]-1 == nxt[0] and cur[1]-1==nxt[1]:
        ans.append(S[cur[0]-1])
    cur[0] = nxt[0]
    cur[1] = nxt[1]
answer = ''.join(reversed(ans))
print(answer)

