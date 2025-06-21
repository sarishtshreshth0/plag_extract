import sys
input = sys.stdin.readline

def main():
    s = input().strip()
    t = input().strip()
    n = len(s)
    m = len(t)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            if s[i-1] == t[j-1]:
                dp[i][j] = max(dp[i-1][j-1] + 1, dp[i][j])
    
    ans_r = []
    while n > 0 and m > 0:
        if dp[n][m] == dp[n-1][m]: n -= 1
        elif dp[n][m] == dp[n][m-1]: m -= 1
        else:
            n -= 1
            m -= 1
            ans_r.append(s[n])
    print("".join(reversed(ans_r)))

if __name__ == '__main__':
    main()