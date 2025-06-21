from _collections import deque
n,m,k=map(int,input().split())

fre=[[] for _ in range(n+1)]
bro=[[] for _ in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    fre[a].append(b)
    fre[b].append(a)

for i in range(k):
    a, b = map(int, input().split())
    bro[a].append(b)
    bro[b].append(a)

ans=[]

x=[-1]*(n+1)

for i in range(1,n+1):
    if x[i]==-1:
        x[i]=i
        data=deque([i])
        while len(data)>0:
            p=data.popleft()
            for j in fre[p]:
                if x[j]==-1:
                    x[j]=i
                    data.append(j)
g=[0]*(n+1)
for i in range(1,n+1):
    g[x[i]]+=1
for i in range(1,n+1):
    g[i]=g[x[i]]

for i in range(1,n+1):
    aa=g[i]-1
    aa-=len(fre[i])
    for j in bro[i]:
        if x[i]==x[j]:
            aa-=1
    ans.append(str(aa))
print(" ".join(ans))

