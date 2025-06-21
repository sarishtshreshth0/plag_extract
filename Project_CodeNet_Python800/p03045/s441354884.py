n,m=map(int,input().split())
xy=[list(map(int,input().split())) for _ in range(m)]
ans=[1]*n
a=list(range(n))
def find(a, x):
    if a[x] != x:
        a[x] = find(a, a[x])
    return a[x]
 
 
def unite(a, x, y):
    x = find(a, x)
    y = find(a, y)
    if x != y:
        a[x] = min(x, y)
        a[y] = a[x]
 
for i,j ,k in xy:
    unite(a,i-1,j-1)
q=[]
for i in range(n):
    p=find(a,i)
    q.append(p)
print(len(set(q)))