import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


s = input()
t = input()

def sub(s,t):
    """共通部分文字列長
    """
    ls = len(s)
    lt = len(t)
    dp = [[0]*(lt+1) for _ in range(ls+1)]
    ###
    prev = [[None]*(lt+1) for _ in range(ls+1)]
    ###
    for i in range(1,ls+1):
        for j in range(1,lt+1):
            if dp[i][j-1]>dp[i-1][j]:
                v = dp[i][j-1]
                pp = (i,j-1)
            else:
                v = dp[i-1][j]
                pp = (i-1,j)
            if s[i-1]==t[j-1] and dp[i-1][j-1] + 1 > v:
                v = dp[i-1][j-1] + 1
                pp = (i-1,j-1)
            dp[i][j] = v
            ###
            prev[i][j] = pp
            ###
    return dp, prev

dp, prev = sub(s,t)
ans = []
i,j = len(s), len(t)
while prev[i][j] is not None:
    if prev[i][j]==(i-1, j-1):
        ans.append(s[i-1])
    i,j = prev[i][j]
print("".join(ans[::-1]))