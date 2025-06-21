from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)
def solve():
    N = int(input())
    G = defaultdict(list)

    for i in range(N-1):
        a, b = map(int,input().split())
        a -= 1
        b -= 1
        G[a].append((b,i))
        G[b].append((a,i))
    
    res = [0] * (N-1)
    dfs(0,-1,-1,G,res)
    print(max(res))
    print(*res, sep='\n')
    
def dfs(v,p,pc,G,res):
    next_c = 1
    for next_v, num in G[v]:
        if next_v == p:
            continue
        if next_c == pc:
            next_c += 1
        
        res[num] = next_c
        dfs(next_v,v,next_c,G,res)
        
        next_c += 1

if __name__ == '__main__':
    solve()