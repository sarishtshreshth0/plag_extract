s,t='0'+input(),'0'+input()
ns,nt=len(s)+1,len(t)+1
dp=[[0 for i in range(nt)] for i in range(ns)]
for i in range(1,ns):
	for j in range(1,nt):
		if s[i-1]==t[j-1]:dp[i][j]=dp[i-1][j-1]+1
		else:dp[i][j]=max(dp[i-1][j],dp[i][j-1])
i,j=ns-1,nt-1
ans=''
while i>0 or j>0:
	if dp[i][j]==dp[i][j-1]:j-=1
	elif dp[i][j]==dp[i-1][j]:i-=1
	else:
		ans=s[i-1]+ans
		i-=1;j-=1
print(ans[1:])