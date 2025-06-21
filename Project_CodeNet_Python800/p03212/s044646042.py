#dp[i][j][0,1,2,3] 上からi桁目までみた j 01 未確定確定 k でてきてない　３　５　７ 
dic = {7:4,5:2,3:1}
def getdic(n):
    return dic.get(n,0)
N = list(map(int,list(input())))

dp = [[[0]*8 for j in range(0,2,1)]for i in range(0,len(N),1)]

if N[0] in {3,5,7}:
    dp[0][0][getdic(N[0])] = 1
for i in (set(range(0,N[0]))&{3,5,7}):
    dp[0][1][getdic(i)] = 1

for i in range(1,len(N),1):
    dp[i-1][1][0]=1
    #確定から確定
    for k in range(0,8,1):
        dp[i][1][1|k] += dp[i-1][1][k]
        dp[i][1][2|k] += dp[i-1][1][k]
        dp[i][1][4|k] += dp[i-1][1][k]
    #未確定から確定
    for k in range(1,8,1):
        for n in (set(range(0,N[i]))&{3,5,7}):
            dp[i][1][getdic(n)|k] += dp[i-1][0][k]
    #未確定から未確定
    if N[i] in {7,5,3}:
        for k in range(0,8,1):
            dp[i][0][getdic(N[i])|k] += dp[i-1][0][k]

print(dp[len(N)-1][0][7]+dp[len(N)-1][1][7])
