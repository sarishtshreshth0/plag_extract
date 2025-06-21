n = int(input())
aka = []
ao = []
aka = aka + [list(map(int,input().split())) for _ in range(n)]
ao = ao + [list(map(int,input().split())) for _ in range(n)]

aka = sorted(aka, key=lambda x:x[1],reverse=True)
ao = sorted(ao, key=lambda x:x[0])

ans = 0

for i in range(n):
	for j in range(n):
		if ao[i][0] > aka[j][0] and ao[i][1] > aka[j][1]:
			ans += 1
			aka[j][1] = 201
			break

print(ans)