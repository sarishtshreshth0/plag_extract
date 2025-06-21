s = input()
t = input()

maxLength = [[0 for i in range(len(s)+2)] for j in range(len(t)+2)] # index_s, index_t

for i_t in range(1,len(t)+1) :
	for i_s in range(1,len(s)+1) :
		if s[i_s-1] == t[i_t-1] :
			maxLength[i_t][i_s] = max(maxLength[i_t-1][i_s-1] + 1, maxLength[i_t][i_s])
		maxLength[i_t+1][i_s] = max(maxLength[i_t+1][i_s], maxLength[i_t][i_s])
		maxLength[i_t][i_s+1] = max(maxLength[i_t][i_s+1],maxLength[i_t][i_s])

str = ''
i, j = len(t), len(s)

while( i > 0 and j > 0) :
	if maxLength[i][j] == maxLength[i-1][j] :
		i -= 1

	elif maxLength[i][j] == maxLength[i][j-1] :
		j -= 1

	else :
		str = s[j-1] + str # (j + 1)文字目
		i -= 1
		j -= 1

print(str)