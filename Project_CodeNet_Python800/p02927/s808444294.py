m, d = map(int, input().split())
D = [str(i) for i in range(1,d+1)]
c = 0

for i in range(1, m+1):
	for j in D:
		if len(j) == 2 and int(j[0]) >= 2 and int(j[1]) >= 2:
			
			if i == int(j[0]) * int(j[1]):
					
				c += 1

print(c)