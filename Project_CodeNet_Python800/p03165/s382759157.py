import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def main():
    S = readline().strip()
    T = readline().strip()
    N, M = len(S), len(T)

    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(M):
            if S[i] == T[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            elif dp[i + 1][j] > dp[i][j + 1]:
                dp[i + 1][j + 1] = dp[i + 1][j]
            else:
                dp[i + 1][j + 1] = dp[i][j + 1]

    ans = []
    i, j = N, M
    while i and j:
        if S[i - 1] == T[j - 1]:
            ans.append(S[i - 1])
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1
        else:
            i -= 1

    print(''.join(reversed(ans)))
    return


if __name__ == '__main__':
    main()
