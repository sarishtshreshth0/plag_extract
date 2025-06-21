from collections import deque
n = int(input())
edges=[[]for i in range(n)]
nodes=[None]*n
for i in range(1,n):
    a , b = map(int, input().split())
    edges[a-1].append(i)
    edges[b-1].append(i)
    nodes[i]=(a-1,b-1)
ma =0
for i in range(n):
    ma=max(ma,len(edges[i]))

col=[None]*n
d = deque([(0,0)])
while d:
    t=1
    v , ex_col = d.pop()
    for i in edges[v]:
        if col[i] is None:
            if t==ex_col:
                t+=1
            col[i]=t
            a1,b1=nodes[i]
            if a1==v:
                d.append((b1,t))
            else:
                d.append((a1,t))
            t+=1

print(ma)
for i in range(1,n):
    print(col[i])
