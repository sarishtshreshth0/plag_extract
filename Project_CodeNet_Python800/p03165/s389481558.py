import numpy as np


def main():
    S = np.array(list(input()))
    LS = len(S)
    T = np.array(list(input()))
    LT = len(T)
    # LCS
    dp = np.zeros((LS + 1, LT + 1))
    match = S.reshape(-1, 1) == T.reshape(1, -1)
    for s in range(LS):
        dp[s + 1, 1:] = np.fmax(dp[s, :(-1)] + match[s], dp[s, 1:])
        dp[s + 1] = np.maximum.accumulate(dp[s + 1])
    # recover
    s, t = LS, LT
    ans = ''
    while s > 0 and t > 0:
        if dp[s, t] == dp[s - 1, t]:
            s -= 1
        elif dp[s, t] == dp[s, t - 1]:
            t -= 1
        else:
            ans = S[s - 1] + ans
            s -= 1
            t -= 1
    print(ans)


if __name__ == '__main__':
    main()