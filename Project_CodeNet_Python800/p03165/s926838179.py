s = input()
t = input()
dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
for i in range(len(s)):
    for j in range(len(t)):
        if s[i]==t[j]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            if dp[i+1][j] < dp[i][j+1]:
                dp[i+1][j+1] = dp[i][j+1]
            else:
                dp[i+1][j+1] = dp[i+1][j]

i = len(s)-1
j = len(t)-1
ans = ''                
while i>=0 and j>=0:
    if s[i]==t[j]:
        ans += t[j]
        i -= 1
        j -= 1
    else:
        if dp[i][j+1]>dp[i+1][j]:
            i -= 1
        else:
            j -= 1
print(ans[::-1])