s = list(input())
s = [''] + s
t = list(input())
t = [''] + t
dp = [[0] * (len(t)) for _ in range(len(s))]

# dpテーブル作成

for i in range(1, len(s)):
    for j in range(1, len(t)):

        if s[i] == t[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 

answer_len = dp[len(s)-1][len(t)-1]

# dpテーブル逆走
answer = [0] * answer_len
i = len(s) -1
j = len(t) -1

while True:
    if dp[i][j] - dp[i-1][j-1] == 1 and dp[i][j] - dp[i][j-1] == 1 and dp[i][j] - dp[i-1][j] == 1:
        answer[answer_len-1] = s[i]
        answer_len -= 1
        i -= 1
        j -= 1
        if answer[0] != 0:
            break
    elif dp[i][j] - dp[i][j-1] == 1 and dp[i][j] - dp[i-1][j] != 1:
        i -= 1
    elif dp[i][j] - dp[i][j-1] != 1 and dp[i][j] - dp[i-1][j] == 1:
        j -= 1
    else:
        j -= 1

    if j == 0:
        j += 1
        i -= 1
    
    if i == 0:
        break
 
print(''.join(answer))