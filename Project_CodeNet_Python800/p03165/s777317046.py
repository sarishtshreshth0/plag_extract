import sys
def main():
    s=list(sys.stdin.readline().strip())
    t=list(sys.stdin.readline().strip())
    S,T=len(s),len(t)
    dp=[[0 for _ in range(T+1)] for _ in range(S+1)]
    for i in range(S):
        for j in range(T):
            if s[i]==t[j]:dp[i+1][j+1]=dp[i][j]+1
            dp[i+1][j+1]=max(dp[i+1][j+1],dp[i+1][j],dp[i][j+1])
    res=''
    i,j=S,T
    while i>0 and j>0:
        if dp[i][j]==dp[i-1][j]:i-=1
        elif dp[i][j]==dp[i][j-1]:j-=1
        else:
            res=s[i-1]+res
            i,j=i-1,j-1
    print(res)
if __name__=='__main__':main()