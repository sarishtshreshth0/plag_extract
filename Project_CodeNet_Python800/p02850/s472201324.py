import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**18
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())

    N = NI()
    root = [[] for _ in range(N)]
    node = [0] * N
    color = [0] * (N-1)
    for i in range(N-1):
        a,b = LI()
        root[a-1].append((b-1,i))
        root[b-1].append((a-1,i))

    q = [(0,0)]
    ans = 0
    while q:
        i,c = q.pop()
        node[i] = 1
        next_c = 1
        for d,x in root[i]:
            if node[d]: continue
            if next_c == c: next_c += 1
            color[x] = next_c
            ans = max(ans,next_c)
            q.append((d,next_c))
            next_c += 1
    print(ans)
    print(*color,sep='\n')

if __name__ == '__main__':
    main()