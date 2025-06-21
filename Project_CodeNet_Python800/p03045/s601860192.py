n,m=map(int,input().split())
def root(x):
	if x!=parent[x]:
		x=root(parent[x])
	return x
def same(x,y):
	return root(x)==root(y)
parent=list(range(n))
rank=[0]*n
def unite(x,y):
	rx=root(x)
	ry=root(y)
	if rank[rx]>rank[ry]:
		parent[ry]=rx
	else:
		parent[rx]=ry
		if rank[rx]==rank[ry]:
			rank[ry]+=1

for i in range(m):
	x,y,z=map(int,input().split())
	unite(x-1,y-1)
ans=set()
for i in range(n):
	ans.add(root(i))
print(len(ans))