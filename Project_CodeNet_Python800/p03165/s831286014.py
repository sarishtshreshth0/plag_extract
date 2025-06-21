### The code is worked in dp, with a 2D matrix technique.

s = input()
t = input()

dp = [[0 for i in range(len(s)+1)] for j in range(len(t)+1)]
s = "0"+s
t = "0"+t

q = []

for i in range(1, len(t)):
    for j in range(1, len(s)):
        if s[j] == t[i]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

i = len(t)-1
j = len(s)-1

while i != 0 and j != 0:
    if dp[i][j] != dp[i-1][j] and  dp[i][j] != dp[i][j-1]:
        q.append(t[i])
        i -= 1
        j -= 1
    elif dp[i][j] != dp[i-1][j] and  dp[i][j] == dp[i][j-1]:
        j -= 1
    elif dp[i][j] == dp[i-1][j] and  dp[i][j] != dp[i][j-1]:
        i -= 1
    else:
        i -= 1

print(''.join(q[::-1]))


