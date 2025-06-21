s=input()
N=len(s)
t=input()
M=len(t)

alphabetlist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def al(str):
    return alphabetlist.index(str)+1

dp=[[0 for i in range(0,M+1)] for i in range(0,N+1)]

for i in range(0,N):
    for j in range(0,M):
        if s[i]==t[j]:
            dp[i+1][j+1]=dp[i][j]+1
        else:
            if dp[i+1][j]>dp[i][j+1]:
                dp[i+1][j+1]=dp[i+1][j]
            else:
                dp[i+1][j+1]=dp[i][j+1]

ans=[]
i=N
j=M
while i>0 and j>0:
    if dp[i][j]==dp[i-1][j]:
        i-=1
    elif dp[i][j]==dp[i][j-1]:
        j-=1
    else:
        ans.append(s[i-1])
        i-=1
        j-=1

ans=ans[::-1]
print(''.join(ans))