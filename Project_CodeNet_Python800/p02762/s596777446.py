import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(2*100)

def main():
    
    N, M, K = map(int, input().split())
    G = {v: deque([]) for v in range(N)}
    G_original = {v: deque([]) for v in range(N)}
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
        G_original[a].append(b)
        G_original[b].append(a)

    Block = {v: deque([]) for v in range(N)}
    for _ in range(K):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        Block[c].append(d)
        Block[d].append(c)

    # seen = [0]*(N)
    stack = []
    color = {v: None for v in range(N)}
    col2v = {col: set() for col in range(N)}
    
    def dfs(j, col):
        if color[j] is not None:
            return
        # seen[j] = 1
        col2v[col] = set()
        stack.append(j)
        color[j] = col
        col2v[col].add(j)
        while stack:
            s = stack[-1]
            if not G[s]:
                stack.pop()
                continue
            g_NO  = G[s].popleft()
            if color[g_NO] is not None:
                continue
            color[g_NO] = col
            col2v[col].add(g_NO)
            # color[g_NO] = 1
            stack.append(g_NO)
    # def dfs(node, co):
    #     if color[node] is not None:
    #         return
        
    #     color[node] = co
    #     col2v[co].add(node)
    #     for n in G[node]:
    #         dfs(n, co)
    #     return
        
    c = 0
    for start in range(N):
        dfs(start, c)
        c += 1
    
    ans = []
    for v in range(N):
        # kouho = col2v[color[v]]
        # # print(kouho)
        # block = Block[v]
        # # print(block)
        # friend = G_original[v]
        # # print(friend)
        # tmp = kouho - set(block + friend)
        tmp = col2v[color[v]]
        tmp2 = tmp & set(Block[v])
        tmp3 = tmp & set(G_original[v])
        print((len(tmp)-len(tmp2)-len(tmp3)-1), end=" ")
        # ans.append(len(col2v[color[v]] - set(Block[v]+G_original[v]))-1)
        
        # print("##############")
    # print(*ans)
main()