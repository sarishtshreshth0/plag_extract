def resolve():
	m,d=map(int,input().split())
	cnt=0
	for i in range(1,m+1):
	    for j in range(10,d+1):
	        if (j//10)*(j%10)==i and j//10>1 and j%10>1:
	            cnt+=1
	print(cnt)
resolve()