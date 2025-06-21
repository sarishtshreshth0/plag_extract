import queue

N=int(input())
G=[[] for index1 in range(N+1)]
for index in range(1,N):
    a,b=map(int,input().split())
    G[a].append((b,index))
    G[b].append((a,index))

#A[i]=辺iの色
A=[0]*N
q=queue.Queue()

#bfs
#(ノード、色、親)
q.put((1,0,0))
while not q.empty():
    now=q.get()
    i=1 #色
    for next in G[now[0]]:
        if next[0]==now[2]: #親
            continue
        else:
            if i==now[1]:
                i+=1
            A[next[1]]=i    #色を定める
            q.put((next[0],i,now[0]))
            i+=1

    #print(now,(next[0],i,now[0]))


print(max(A))
for j in range(N-1):
    print(A[j+1])


    




