#nord_aで使っている色の＋１
#初期入力
import sys
input = sys.stdin.readline
#from collections import deque
import heapq
N = int(input())
connection   ={i:set() for i in range(1,N+1)}
A            =[[i] for i in range(N-1)]
A_sort =sorted(A)
for i in range(N-1):
    a,b = (int(x) for x in input().split())
    connection[a].add(b) # つながりを逆向きも含めて入力
    connection[b].add(a) # 
    A_sort[i].append((a,b))             #色を出力するため
A_sort.sort(key=lambda x:x[1])
#色の数(各頂点の最大値)
color_max =0
for i in connection.values():
    color_max =max(color_max, len(i) )

#各頂点に色を準備⇒辺の色決定
aa=[]
hq_none =heapq.heapify(aa)
color_node ={i:[] for i in range(1,N+1)} #頂点に使った色の管理,dequeで高速？
for i in range(1,N+1):
    heapq.heapify(color_node[i])
color_edge =[0]*(N-1)

for i in range(N-1):
    n_a,n_b = A_sort[i][1] #i番目の辺とつながっている頂点
    if color_node[n_a] ==[]:
        color =0
    else:
        color =(color_node[n_a][0]) -1
    while True:
        #color +=1
        q,color =divmod(color,(-1)*color_max)
        if color not in color_node[n_a] and color not in color_node[n_b]: 
            #color_edge[i] =color+1          #辺の色を出力用に決める。1～color_max
            A_sort[i].append((-1)*color+1)     #辺の色を出力用に決める。1～color_max,A_sortに入れて、再度ソート
            heapq.heappush(color_node[n_a],color)    #前の頂点に使った色を追加、
            heapq.heappush(color_node[n_b],color)    #heapqの最大値出したいので*(-1)

            break
        else:
            color -=1      
#出力
print(color_max)
A_sort.sort()
for i in A_sort:
    print(i[2])