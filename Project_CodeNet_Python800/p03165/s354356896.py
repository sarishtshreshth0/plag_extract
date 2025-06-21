s = [""]+list(input())
t = [""]+list(input())
dp = [[0 for x in range(len(s))] for x in range(len(t))]
for y in range(1,len(t)):
    for x in range(1,len(s)):
        if(t[y] == s[x]):
            dp[y][x] = dp[y-1][x-1]+1
        else:
            dp[y][x] = max(dp[y-1][x],dp[y][x-1])
y,x = len(t)-1,len(s)-1
ans = []
while(dp[y][x] > 0):
    if(dp[y][x] == dp[y-1][x]):
        y -= 1
    elif(dp[y][x] == dp[y][x-1]):
        x -= 1
    else:
        ans.append(s[x])
        y -= 1
        x -= 1
ans.reverse()
print("".join(ans))
