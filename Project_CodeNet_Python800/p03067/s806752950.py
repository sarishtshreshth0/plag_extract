a,b,c=list(map(int ,input().split()))
ans_range=range(a,b)
ans_range1=range(b,a)
if(c in ans_range or c in ans_range1):
	print("Yes")
else:
	print("No")
