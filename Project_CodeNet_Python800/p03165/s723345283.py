import sys
input = sys.stdin.readline

s = input()[:-1]
t = input()[:-1]
dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]

for i in range(len(s)):
    for j in range(len(t)):
        if s[i]==t[j]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            if dp[i+1][j]>dp[i][j+1]:
                dp[i+1][j+1] = dp[i+1][j]
            else:
                dp[i+1][j+1] = dp[i][j+1]

ci, cj = len(s), len(t)
ans = []

while ci!=0 and cj!=0:
    if s[ci-1]==t[cj-1]:
        ci -= 1
        cj -= 1
        ans.append(s[ci])
    else:
        if dp[ci][cj]==dp[ci-1][cj]:
            ci -= 1
        else:
            cj -= 1

ans.reverse()
print(''.join(ans))