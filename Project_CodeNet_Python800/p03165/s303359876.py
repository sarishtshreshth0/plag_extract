import sys
sys.setrecursionlimit(2147483647)
INF = float("inf")
MOD = 10**9 + 7 # 998244353
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    S = input()
    T = input()
    m = len(S)
    n = len(T)
    dp = [[-INF] * (n + 1) for _ in range(m + 1)]
    prev = [[(-1, -1)] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
        dp[i][0] = 0
    for j in range(n):
        dp[0][j] = 0

    for i in range(m):
        for j in range(n):
            if S[i] == T[j]:
                if dp[i + 1][j + 1] < dp[i][j] + 1:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                    prev[i + 1][j + 1] = (i, j)
            else:
                if dp[i + 1][j + 1] < dp[i + 1][j]:
                    dp[i + 1][j + 1] = dp[i + 1][j]
                    prev[i + 1][j + 1] = (i + 1, j)
                if dp[i + 1][j + 1] < dp[i][j + 1]:
                    dp[i + 1][j + 1] = dp[i][j + 1]
                    prev[i + 1][j + 1] = (i, j + 1)

    i, j = m, n
    res = []
    cnt = 0
    while 1:
        pi, pj = prev[i][j]
        if (pi, pj) == (-1, -1):
            break
        if i - pi == 1 and j - pj == 1:
            res.append(S[pi])
        i, j = pi, pj

    print(''.join(reversed(res)))
resolve()