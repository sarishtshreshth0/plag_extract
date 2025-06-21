s = input()
t = input()

dp = [[0]*(1+len(s)) for i in range(1+len(t))]

for i in range(1, 1+len(t)):
    for j in range(1, 1+len(s)):
        if s[j-1] == t[i-1]:
            dp[i][j] = 1+dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

i = len(t)
j = len(s)
st = ""

while dp[i][j] != 0:
    if s[j-1] == t[i-1]:
        st += s[j-1]
        i -= 1
        j -= 1
    else:
        if dp[i][j-1] > dp[i-1][j]:
            j -= 1
        else:
            i -= 1
            
print(st[::-1])