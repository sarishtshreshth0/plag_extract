import sys


def input(): return sys.stdin.readline().rstrip()


S = input()
T = input()
dp = [[0]*(len(T)+1) for j in range(len(S)+1)]
# dp[i][j] := i,j までの最大のもの。(length)
for i in range(len(S)):
    for j in range(len(T)):
        if S[i] == T[j]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            if dp[i+1][j] >= dp[i][j+1]:
                dp[i+1][j+1] = dp[i+1][j]

            elif dp[i+1][j] < dp[i][j+1]:
                dp[i+1][j+1] = dp[i][j+1]
X, Y = len(S), len(T)
ans = []
while dp[X][Y]:
    if S[X-1] == T[Y-1]:
        ans.append(S[X-1])
        X -= 1
        Y -= 1
    else:
        if dp[X-1][Y] >= dp[X][Y-1]:
            X -= 1
        else:
            Y -= 1
            continue
ans.reverse()
print("".join(ans))