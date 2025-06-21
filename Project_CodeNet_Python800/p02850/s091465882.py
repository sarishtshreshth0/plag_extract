import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from collections import deque 

class Edge:
    def __init__(self, to, id):
        self.to = to
        self.id = id

def main():
    
    n = int(readline())
    g = [[] for _ in range(n)]

    for i in range(n-1):
        a, b = map(int, readline().split())
        g[a-1].append(Edge(b-1, i))
        g[b-1].append(Edge(a-1, i))

    dq = deque()    
    done = [0 for _ in range(n)]
    dq.append(0)
    done[0] = 1
    edgecolor = [0 for _ in range(n-1)]

    while len(dq) > 0: 
        v = dq.pop()
        c = -1
        for i in range(len(g[v])):
            nx = g[v][i].to
            edge_id = g[v][i].id
            if done[nx]:
                c = edgecolor[edge_id]
        k = 1
        for i in range(len(g[v])):
            nx = g[v][i].to
            edge_id = g[v][i].id
            if done[nx]:
                continue
            if k == c:
                k += 1
            edgecolor[edge_id] = k
            k += 1  
            done[nx] = 1
            dq.append(nx)

    mx = max(edgecolor) 
    print(mx)
    for ec in edgecolor:
        print(ec)

if __name__ == '__main__':
    main()
