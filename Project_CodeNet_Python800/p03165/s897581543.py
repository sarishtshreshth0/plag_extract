from sys import stdin
s,t = stdin.readline().strip(),stdin.readline().strip()
dp = [[0]*len(s) for _ in range(len(t))]
maxi = [0]*len(s)
for i,val in enumerate(t):
    maxi1 = []
    for x in range(len(s)):
        if s[x] == val:
            dp[i][x] = (0 if x==0 else maxi[x-1])+1
        maxi1.append(max((0 if x==0 else maxi1[x-1]),dp[i][x]))
    for j in range(len(maxi)):
        maxi[j] = max(maxi[j],maxi1[j])
n = max(map(max,dp))
ans,i,j = [],len(t)-1,len(s)-1
while n:
    fl = 0
    for x in range(i,-1,-1):
        for y in range(j,-1,-1):
            if dp[x][y] == n:
                ans.append(s[y])
                fl = 1
                i,j = x-1,y-1
                break
        if fl:
            break
    n -= 1
print(''.join(ans[::-1]))