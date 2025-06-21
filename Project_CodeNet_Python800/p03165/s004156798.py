import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = readline().rstrip().decode()
t = readline().rstrip().decode()
s_size = len(s)
t_size = len(t)
dp = [[0] * (t_size + 1) for _ in range(s_size + 1)]
ans = ''
for i in range(s_size):
    for j in range(t_size):
        if s[i] == t[j]:
            if dp[i + 1][j + 1] < dp[i][j] + 1:
                dp[i + 1][j + 1] = dp[i][j] + 1
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i + 1][j], dp[i][j + 1])
while s_size > 0 and t_size > 0:
    if dp[s_size][t_size] == dp[s_size - 1][t_size]:
        s_size -= 1
    elif dp[s_size][t_size] == dp[s_size][t_size - 1]:
        t_size -= 1
    else:
        ans = s[s_size - 1] + ans
        s_size -= 1
        t_size -= 1
print(ans)
