import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
l = 3010
def main():
    s = input().strip()
    t = input().strip()
    dp = [[0] * l for i in range(l)]
    rdp = [[0] * l for i in range(l)]
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + 1
                rdp[i][j] = (i-1, j-1)
            else:
                if dp[i-1][j] < dp[i][j-1]:
                    dp[i][j] = dp[i][j-1]
                    rdp[i][j] = (i, j-1)
                else:
                    dp[i][j] = dp[i-1][j]
                    rdp[i][j] = (i-1, j)

    # print(dp[len(s)-1][len(t)-1])
    ans = ''
    p, q = len(s)-1, len(t)-1
    while True:
        if p == -1 or q == -1:
            break
        nextp, nextq = rdp[p][q]
        if nextp != p and nextq != q:
            ans += s[p]
        p = nextp
        q = nextq

    print(''.join(reversed(ans)))
if __name__ == '__main__':
    main()
