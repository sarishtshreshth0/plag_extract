
import sys
sys.setrecursionlimit(10 ** 7)

def resolve():
    N, M,K = map(int, input().split())
    frind = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x:int(x)-1, input().split())
        frind[a].append(b)
        frind[b].append(a)

    block = [[] for _ in range(N)]
    for _ in range(K):
        a, b = map(lambda x: int(x) - 1, input().split())
        block[a].append(b)
        block[b].append(a)


    D = {}
    parent = [-1]*N
    visited = [False]*N
    for root in range(N):
        if visited[root]:
            continue
        D[root] = set([root])
        stack = [root]
        while stack:
            n = stack.pop()
            visited[n] = True
            parent[n] = root
            for to in frind[n]:
                if visited[to]:
                    continue
                D[root].add(to)
                stack.append(to)

    ans = [0]*N
    for i in range(N):
        gr = D[parent[i]]
        tmp = len(gr)-len(frind[i]) - 1
        for bl in block[i]:
            if bl in gr:
                tmp -= 1
        ans[i] = tmp
    print(*ans)


if __name__ == "__main__":
    resolve()
