n,m=map(int,input().split())
    
root=[int(i) for i in range(n)] 
rank=[0]*n    
def find(x):
    if root[x]==x:
        return x 
    else:
        return find(root[x])

for i in range(m):
    x,y,z=map(int,input().split())
    fx=find(x-1)
    fy=find(y-1)
    if rank[fx]>=rank[fy]:
        root[fy]=fx
        if rank[fx]==rank[fy]:
            rank[fx]+=1
    else:
        root[fx]=fy 
a=[]
for i in range(n):
    a.append(find(i)) 
print(len(set(a)))