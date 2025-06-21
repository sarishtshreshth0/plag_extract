"""2020/7/2再挑戦"""
#幅優先探索 親の頂点と色を覚えておく。親の色を除く＋1ずつ足していく。color_maxを超えたら余りをとる。
from collections import deque
N = int(input())
connection ={i:set() for i in range(1,N+1)}
connection_parent =[]
for i in range(1,N):
    a,b = (int(i) for i in input().split())
    connection[a].add(b)
    connection[b].add(a)
    connection_parent.append(b)

#最小の色数
c =[]
for i in connection.values():
    c.append(len(i))
color_min =max(c)

#幅優先探索
start =1
color={i:0 for i in range(1,N+1)} #P:今の頂点と次への辺の色を記録(tuple)。
passed =set() # 通過した記録
dq =deque([start]) #スタートは1でいいのか？
color[start] =0
while len(dq) >0:
    now =dq.popleft()
    passed.add(now)
    c1 =color[now]
    for next in connection[now]:
        if next not in passed:
            c1 +=1
            c1 %=color_min
            color[next] =c1  #0 <=c <= color_min-1のため　＋１
            dq.append(next)
print(color_min)
for i in connection_parent:
    print(color[i] +1)