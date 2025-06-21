s=input()
t=input()

dp=[[-1]*(len(t)+1) for x in range(len(s)+1)]
arr = ""
for i in range(len(s),-1,-1):
    for j in range(len(t),-1,-1):
        if i>=(len(s)) or j>=(len(t)):
            dp[i][j] = 0
        else:
            if s[i] == t[j]:
                dp[i][j] = dp[i+1][j+1] + 1
            else:
                dp[i][j] = max(dp[i+1][j],dp[i][j+1])

l=dp[0][0]
i,j=0,0
while len(arr)!=l:
    if s[i] == t[j]:
        arr=arr+s[i]
        i+=1
        j+=1
    else:
        if dp[i+1][j]>=dp[i][j+1]:
            i+=1
        else:
            j+=1

print(arr)



# def func(i,j):
    # if i>=(len(s)) or j>=(len(t)):
    #     return 0
    # if dp[i][j]!=-1:
    #     return dp[i][j]
    # if s[i]==t[j]:
    #     dp[i][j] = func(i+1,j+1)+1
    #     return dp[i][j]
    # if s[i]!=t[j]:
    #     dp[i][j] = max(func(i+1,j),func(i,j+1))
    #     return dp[i][j]
# l=func(0,0)
