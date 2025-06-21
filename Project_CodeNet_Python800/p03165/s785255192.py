s,t=input(),input()
S,T=len(s),len(t)

DP=[[0 for _ in range(T+1)] for _ in range(S+1)]
for i in range(1,S+1):
    for j in range(1,T+1):
        if s[i-1]==t[j-1]:DP[i][j]=DP[i-1][j-1]+1
        else:DP[i][j]=max(DP[i-1][j],DP[i][j-1])

ans=""
x,y=S,T
while DP[x][y]!=0:
    if DP[x][y]==DP[x-1][y]:x -=1
    elif DP[x][y]==DP[x][y-1]:y -=1
    else:
        ans +=s[x-1]
        x -=1
        y -=1

print(ans[::-1])