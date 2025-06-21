s=list(input())
t=list(input())
x=len(s)
y=len(t)
dp=[[0]*(y+1) for i in range(x+1)]

for i in range(x):
    for j in range(y):
        if s[i]==t[j]:
            dp[i+1][j+1]=dp[i][j]+1
        else:
            dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])

# 文字列の復元、後ろから見て、目的の数字見つけたら斜め上に飛ぶ
v=dp[-1][-1]
# tの飛んだ時がtの何文字目かを記録する
ans=''
while x>0 and y>0:
    # 左に移動
    if dp[x][y]==dp[x][y-1]:
        y-=1
    # 下に移動
    elif dp[x][y]==dp[x-1][y]:
        x-=1
    # 斜めに移動
    else:
        x-=1
        y-=1
        ans=t[y]+ans
print(ans)