import queue 
N = int(input())
tree = [[]for _ in range(N+1)]
for i in range(1,N):
    a,b = map(int,input().split())
    tree[a].append( [b,i])
    tree[b].append([a,i])
 
que = queue.Queue()
node = [-1]*(N+1)
edge = [-1]*N
que.put(1)
node[1] = 1
maxi = 1
start = 0
color = [[] for _ in range(N+1)]
node[1] = 0
while(True):
    if que.empty():
        break
    before = start
    start = que.get()
    col =1
    for i in tree[start]:
        
        if node[i[0]] == -1 :
            que.put(i[0])
        if edge[i[1]] == -1:
            if col == node[start]:
                col += 1
            edge[i[1]] = col
            node[i[0]] = col
            if col > maxi:
                maxi = col
            col +=1
            
print(maxi)
for i in edge[1:]:
    print(i)