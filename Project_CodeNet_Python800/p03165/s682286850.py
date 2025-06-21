from collections import deque

s = input()
t = input()
ls = len(s)
lt = len(t)
DP_len = [[0] * (lt + 1) for i in range(ls + 1)]
Prev =[[0] * (lt + 1) for i in range(ls + 1)]
for i in range(1, ls + 1):
    for j in range(1, lt + 1):
        if s[i - 1] == t[j - 1]:
            if max(DP_len[i - 1][j - 1] + 1, DP_len[i][j - 1], DP_len[i - 1][j]) == DP_len[i-1][j-1] + 1:
                DP_len[i][j] = DP_len[i-1][j-1] + 1
                Prev[i][j] = (i-1, j-1)
            else:
                if DP_len[i][j - 1] >= DP_len[i - 1][j]:
                    DP_len[i][j] = DP_len[i][j - 1]
                    Prev[i][j] = (i, j - 1)
                else:
                    DP_len[i][j] = DP_len[i - 1][j]
                    Prev[i][j] = (i - 1, j)

        else:
            if DP_len[i][j - 1] >= DP_len[i - 1][j]:
                DP_len[i][j] = DP_len[i][j - 1]
                Prev[i][j] = (i, j-1)
            else:
                DP_len[i][j] = DP_len[i - 1][j]
                Prev[i][j] = (i - 1, j)

x = ls
y = lt
ans = ''
while True:
    if x == 0 or y == 0:
        break
    nx, ny = Prev[x][y]
    if (nx != x) and (ny != y):
        ans = s[x-1] + ans
    x = nx
    y = ny
print(ans)
