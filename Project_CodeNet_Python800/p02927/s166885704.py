m,d = map(int,input().split())

ans = 0

for i in range(2,m+1):
	for j in range(d+1):
		if i==j//10*(j-(j//10)*10) and j>=20 and j-(j//10)*10>=2:
			#print(i,j)
			ans = ans + 1
			#print(j//10,(j-(j//10)*10))
print(ans)