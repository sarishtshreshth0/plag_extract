s=input() 
t=input() 
dp=[[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
res=''  
for i in range(1,len(s)+1):
	for j in range(1,len(t)+1):
		if s[i-1]==t[j-1]: 
			dp[i][j]=1+dp[i-1][j-1] 
		else:
			dp[i][j]=max(dp[i-1][j],dp[i][j-1]) 
length=dp[-1][-1] 
res=['']*(length+1)  
i=len(s) 
j=len(t) 
while i>0 and j>0:
	if s[i-1]==t[j-1]:
		res[length-1]=s[i-1] 
		i-=1 
		j-=1 
		length-=1 
	elif dp[i-1][j]>dp[i][j-1]:
		i-=1 
	else:
		j-=1  
print(''.join(res))