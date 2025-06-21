def main():
    S = input()
    T = input()
    dp = [[0] * (len(S) + 1) for _ in range(len(T) + 1)]
    for j, t in enumerate(T, 1):
        for i, s in enumerate(S, 1):
            dp[j][i] = max(dp[j - 1][i], dp[j][i - 1], dp[j - 1][i - 1] + 1 if s == t else 0)
    i, j = len(S), len(T)
    R = ''
    while i > 0 and j > 0:
        n = dp[j][i]
        if dp[j - 1][i] == n:
            j -= 1
        elif dp[j][i - 1] == n:
            i -= 1
        elif dp[j - 1][i - 1] == n - 1:
            j -= 1
            i -= 1
            R += T[j]
        else:
            assert False
    return R[::-1]

print(main())
