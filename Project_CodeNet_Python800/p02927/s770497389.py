M,D = map(int,input().split())

ans=0

for i in range(4,M+1):
	for j in range(22,D+1):

		e =j%10
		f = j//10
		g = e*f

		if e >= 2:
			if g==i:
				ans+=1

print(ans)