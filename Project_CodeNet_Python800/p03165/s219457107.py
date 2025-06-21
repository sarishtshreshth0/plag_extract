s = input()
t = input()
ls = len(s)
lt = len(t)


dp = [[0 for i in range(lt+1)] for j in range(ls+1)]
answer = ''

for i in range(ls):
    for j in range(lt):
        if s[i] == t[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])


i = ls-1
j = lt-1
while (0 <= i) & (0 <= j):
    if s[i] == t[j]:
        answer += s[i]
        i -= 1
        j -= 1
    elif dp[i+1][j+1] == dp[i+1][j]:
        j -= 1
    else:
        i -= 1
if len(answer) == 0:
  print('')
else:
  print(answer[::-1])
