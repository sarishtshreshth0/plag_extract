import sys
input = sys.stdin.readline

s = input()[:-1]
t = input()[:-1]
dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
track = [[-1]*(len(t)+1) for _ in range(len(s)+1)]

for i in range(len(s)):
    for j in range(len(t)):
        if s[i]==t[j]:
            dp[i+1][j+1] = dp[i][j]+1
            track[i+1][j+1] = (i, j)
        else:
            if dp[i+1][j]>dp[i][j+1]:
                dp[i+1][j+1] = dp[i+1][j]
                track[i+1][j+1] = (i+1, j)
            else:
                dp[i+1][j+1] = dp[i][j+1]
                track[i+1][j+1] = (i, j+1)

ci, cj = len(s), len(t)
ans = []

while ci!=0 and cj!=0:
    ni, nj = track[ci][cj]
    
    if ci-ni==1 and cj-nj==1:
        ans.append(s[ni])
    
    ci, cj = ni, nj

ans.reverse()
print(''.join(ans))