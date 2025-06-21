s=input()
t=input()
b=len(t)
a=len(s)


dp=[[0 for i in range(a+1)] for j in range(b+1)]
for i in range(b+1):
	for j in range(a+1):
		if(i==0 or j==0):
			continue
		if(t[i-1]==s[j-1]):
			dp[i][j]=1+dp[i-1][j-1]
		else:
			dp[i][j]=max(dp[i-1][j],dp[i][j-1])
i=b
j=a
l=[]
while(i>0 and j>0):
	if(t[i-1]==s[j-1]):
		l.append(t[i-1])
		i=i-1
		j=j-1
	else:
		if(dp[i-1][j]>dp[i][j-1]):
			i=i-1
		else:
			j=j-1
for i in reversed(l):
    print(i,end='')

    


