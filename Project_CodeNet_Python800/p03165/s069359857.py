import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def longest_common_subsequence(S, T):
    """compute table dp satisfying: 
    dp[i,j] = LCS(S[:i], T[:j])"""
    LS, LT = len(S), len(T)
    dp = np.zeros((LS + 1, LT + 1), np.int32)
    for n in range(1, LS + 1):
        dp[n, 1:] = dp[n - 1, :-1] + (S[n - 1] == T)  # 左上から
        np.maximum(dp[n], dp[n - 1], out=dp[n])  # 上から
        np.maximum.accumulate(dp[n], out=dp[n])  # 左から
    return dp

def reconstruct_LCS(S, T, dp):
    tmp = []
    i, j = len(S), len(T)
    while i > 0 and j > 0:
        if S[i - 1] == T[j - 1]:
            i, j = i - 1, j - 1
            tmp.append(S[i])
        elif dp[i, j] == dp[i - 1, j]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(tmp))

S = np.array(list(readline().decode()), 'U1')[:-1]
T = np.array(list(readline().decode()), 'U1')[:-1]

dp = longest_common_subsequence(S, T)

print(reconstruct_LCS(S, T, dp))
