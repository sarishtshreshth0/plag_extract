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
            vals = [dp[i][j-1], dp[i-1][j]]
            if s[i-1]==t[j-1]:
                vals.append(dp[i-1][j-1] + 1)
            m = max(vals)
            dp[i][j] = m
            ###
            ind = vals.index(m)
            if ind==0:
                prev[i][j] = (i,j-1)
            elif ind==1:
                prev[i][j] = (i-1,j)
            else:
                prev[i][j] = (i-1,j-1)
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