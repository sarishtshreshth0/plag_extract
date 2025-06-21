s,t = input(),input()

S = len(s)
T = len(t)

dp = [[0]*(T+1) for _ in range(S+1)]

for i in range(S):
    for j in range(T):
        dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j],dp[i][j]+(s[i]==t[j]))
    

ans = ''

while S > 0 and T > 0:
    if dp[S][T] == dp[S-1][T]: S -= 1
    elif dp[S][T] == dp[S][T-1]: T -= 1
    else: 
        S -= 1
        T -= 1
        ans = s[S] + ans
print(ans)