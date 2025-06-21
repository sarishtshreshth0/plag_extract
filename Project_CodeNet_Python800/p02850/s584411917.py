from collections import deque
import sys
input =sys.stdin.readline
N = int(input())

#構造入力
color_max =0
connection ={i:deque() for i in range(1,N+1)}
edge_color={}
A =[(-1,-1)]*N
for i in range(1,N):
    a,b = (int(x) for x in input().split())
    connection[a].append(b)
    connection[b].append(a)
    edge_color[(a,b)] =-1
    A[i] =(a,b)
    color_max =max(color_max, len(connection[a]) , len(connection[b]))

#幅優先探索で色塗る
passed =set()
#edge_color ={i:-1 for i in range(1,N+1)}
parent ={i:-1 for i in range(1,N+1)}
parent[1] =0
dq =deque()
dq.append(1)
color =0
#prev =0 #頂点１の親は０とする
edge_color[(0,1)] =0
#node_color[1] =0
while dq:
    now =dq.popleft()
    passed.add(now)
    na_max =max(parent[now],now)
    na_min =min(parent[now],now)
    i_color =edge_color[(na_min,na_max)]
    for next in connection[now]:
        if next in passed:
            continue
        else:
            i_color +=1
            n_max =max(now,next)
            n_min =min(now,next)
            edge_color[(n_min,n_max)] =(i_color)% color_max 
            dq.append(next)
            parent[next] =now
print(color_max)
del edge_color[(0,1)]
for i in range(1,N):
    print(edge_color[A[i]] +1 )