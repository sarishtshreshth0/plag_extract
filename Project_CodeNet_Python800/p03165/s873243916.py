import sys,queue,math,copy,itertools,bisect,collections,heapq
sys.setrecursionlimit(10**7)
INF = 10**18
MOD = 10**9 + 7
LI = lambda : [int(x) for x in sys.stdin.readline().split()]
NI = lambda : int(sys.stdin.readline())

s = input()
t = input()

dp = [[0 for _ in range(len(s)+1)] for _ in range(len(t)+1)]

for i in range(1,len(t)+1):
    for j in range(1,len(s)+1):
        dp[i][j] = max(dp[i][j-1],dp[i-1][j] ,dp[i-1][j-1] + (s[j-1]==t[i-1]))
i = len(t)
j = len(s)
x = dp[i][j]
ans = ''
while i > 0 and j > 0:
    if dp[i][j] == dp[i][j-1]:
        j -= 1
    elif dp[i][j] == dp[i-1][j]:
        i -= 1
    else:
        ans = ''.join([s[j-1],ans])
        i -= 1
        j -= 1
print(ans)