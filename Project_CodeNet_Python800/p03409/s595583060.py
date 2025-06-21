import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())

    N = NI()
    goal = N*2+1
    edge = [set() for _ in range(goal+1)]

    red = [LI() for _ in range(N)]
    blue = [LI() for _ in range(N)]

    for i in range(1,N+1):
        edge[0].add(i)
    for i in range(N+1,goal):
        edge[i].add(goal)

    for i in range(N):
        a,b = red[i]
        for j in range(N):
            c,d = blue[j]
            if a < c and b < d:
                edge[i+1].add(N+j+1)

    ans = 0

    while True:
        q = collections.deque()
        node = [-1] * (goal + 1)
        node[0] = 0
        q.append(0)
        while q:
            u = q.pop()
            for v in edge[u]:
                if node[v] >= 0: continue
                node[v] = u
                if v == goal:
                    ans += 1
                    break
                q.append(v)
            else:
                continue
            break
        else:
            break

        v = goal
        while v > 0:
            u = node[v]
            edge[u].remove(v)
            edge[v].add(u)
            v = u

    print(ans)

if __name__ == '__main__':
    main()