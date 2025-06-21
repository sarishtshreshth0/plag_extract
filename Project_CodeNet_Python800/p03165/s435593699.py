S = input()
T = input()
dp = [[0 for i in range(len(T)+1)] for j in range(len(S)+1)]
for i in range(1,len(S)+1):
    for j in range(1,len(T)+1):
        if S[i-1] == T[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1]) 

length = dp[len(S)][len(T)]
LCS = [0]*length
i = len(S)
j = len(T)
while i > 0 and j > 0: 
    if S[i-1] == T[j-1]: 
        LCS[length-1] = S[i-1]
        i-=1
        j-=1
        length-=1
    elif dp[i-1][j] > dp[i][j-1]: 
        i-=1
    else: 
        j-=1
print("".join(LCS))