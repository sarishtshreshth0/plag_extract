n,m=map(int,input().split())
X=sorted(list(map(int,input().split())))
if n>=m:
	print(0)
	exit()
x=[]
for i in range(len(X)-1):
	x.append(X[i+1]-X[i])
x.sort()
if n==1:print(sum(x))
else:print(sum(x[:-(n-1)]))