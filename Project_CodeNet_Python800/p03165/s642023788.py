def main():
    import sys
    input=sys.stdin.buffer.readline
    s=b' '+input()[:-1]
    t=b' '+input()[:-1]
    n,m=len(s),len(t)
    dp=[[0]*m for _ in range(n)]
    b=dp[0]
    for i,x in enumerate(s[1:],1):
        dpi=dp[i]
        for j,y in enumerate(t[1:],1):
            if x==y:
                dpi[j]=b[j-1]+1
            else:
                v,w=b[j],dpi[j-1]
                dpi[j]=v if v>w else w
        b=dpi
    ans=[]
    i,j=n-1,m-1
    while dp[i][j]:
        if dp[i][j]==dp[i-1][j]:
            i-=1
        elif dp[i][j]==dp[i][j-1]:
            j-=1
        else:
            ans.append(s[i])
            i-=1
            j-=1
    print(''.join(map(chr,ans))[::-1])
main()