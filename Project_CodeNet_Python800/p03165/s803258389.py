import sys
input=sys.stdin.readline
def main():
    s=tuple(input())
    t=tuple(input())
    n=len(s)
    m=len(t)
    dp=[[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n):
        for j in range(m):
            if s[i]==t[j]:
                dp[i+1][j+1]=dp[i][j]+1
            else:
                if dp[i+1][j]>dp[i][j+1]:
                    dp[i+1][j+1]=dp[i+1][j]
                else:
                    dp[i+1][j+1]=dp[i][j+1]
    p=dp[n][m]
    ans=['' for _ in range(p)]
    n-=1
    m-=1
    while p>0:
        if s[n]==t[m]:
            ans[p-1]=s[n]
            n-=1
            m-=1
            p-=1
        elif dp[n+1][m+1]==dp[n][m+1]:
            n-=1
        else:
            m-=1
    print(''.join(ans)) 
if __name__=='__main__':
    main()
