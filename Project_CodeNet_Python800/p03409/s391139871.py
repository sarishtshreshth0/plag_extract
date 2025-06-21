n=int(input())

redlist=[list(map(int,input().split())) for _ in range(n)]
bluelist=[list(map(int,input().split())) for _ in range(n)]

redlist.sort(key = lambda x : x[1], reverse = True)
bluelist.sort(key = lambda x : x[0])


output=0

for blue in bluelist:
	for red in redlist:
		if blue[1] > red[1] and blue[0] > red[0]:
			output+=1
			redlist.remove(red)
			break

print(output)
