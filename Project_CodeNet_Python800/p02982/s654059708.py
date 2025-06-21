import math
n,m = map(int,input().split())
x = [list(map(int,input().split())) for _ in range(n)]
cnt,tmp = 0,0
for i in range(n-1):
	for j in range(i+1,n):
		tmp = 0
		for M in range(m):
			tmp += (x[i][M] - x[j][M])**2
			#print(tmp)
		if math.sqrt(tmp).is_integer():
			cnt += 1
print(cnt)