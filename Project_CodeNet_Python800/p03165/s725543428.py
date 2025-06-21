def solve(s1,s2):
    rows=len(s1)
    cols=len(s2)
    dp=[[0]*(cols+1) for i in range(rows+1)]
    for i in range(1,rows+1):
        for j in range(1,cols+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                
    max_len=dp[rows][cols]
    result=[""]*(max_len+1)
    result[max_len]=""
    i=rows
    j=cols
    while i>0 and j>0:
        if s1[i-1]==s2[j-1]:
            result[max_len-1]=s1[i-1]
            max_len -=1
            i -=1
            j -=1
        elif dp[i-1][j]>dp[i][j-1]:
            i -=1
        else:
            j -=1
    return "".join(result)
            
                
#     if i==n or j==m:
#         return result
#     if s1[i]==s2[j]:
#         result +=s1[i]
#         return result+solve(s1,s2,n,m,i+1,j+1,result)
#     else:
#         left=solve(s1,s2,n,m,i+1,j,result)
#         right=solve(s1,s2,n,m,i,j+1,result)
#         if left:
#             result
        
        ##return max(solve(s1,s2,n,m,i+1,j,result),solve(s1,s2,n,m,i,j+1,result))
s1=input()
s2=input()
n=len(s1)
m=len(s2)
result=""
print(solve(s1,s2))