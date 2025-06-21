import sys
sys.setrecursionlimit(1000000)

n=int(input())
a=[0]*(n-1)
b=[0]*(n-1)

edge=[[] for i in range(n)]
k=0

for i in range(n-1):
    a[i],b[i]=map(int,input().split())
    a[i]-=1
    b[i]-=1
    edge[b[i]].append(a[i])
    edge[a[i]].append(b[i])

color_dict={}

def dfs(x, last=-1, ban_color=-1):
    global k
    color=1
    for to in edge[x]:
        if to==last:
            continue
        if color==ban_color:
            color+=1
        color_dict[(x,to)]=color
        k=max(k,color)
        dfs(to,x,color)
        color+=1
dfs(0)
print(k)

for i in range(n-1):
    if (a[i],b[i]) in color_dict:
        print(color_dict[(a[i],b[i])])
    else:
        print(color_dict[(b[i],a[i])])