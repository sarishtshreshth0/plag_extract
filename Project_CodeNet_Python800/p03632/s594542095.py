A,B,C,D = map(int, input().split())
p=max(A,C)-min(B,D)
if p<=0:
	print(abs(p))
else:
	print(0)