"""
ABC146D Diff: 1175
"""
# BFSで各親の子供をループして調べていく.
# 各ノードの周りにある色を集合で持ったらTLE
# -> 色を塗る規則に注意すれば各親に対してintを1つ用意すれば十分

from collections import deque
import sys
input = sys.stdin.readline
    
def bfs(v, N, G, E):
    #訪れたかどうか
    visited = [0]*N
    queue = deque()
    K = -1
    # 各ノードで使っている色の中で最大の色
    node2color = [-1 for _ in range(N)]
    queue.append(v)
    visited[v] = 1
    while queue:
        q = queue.popleft()
        # 使う色(int)を初期化: 0から++していくことで、
        # 調べる親qの子に対してできるだけ小さい色を塗れる。
        color = 0
        for nex in G[q]:
            if visited[nex]:
                #すでに訪れていたらcontinue
                continue
            visited[nex] = 1
            color += 1
            if color == node2color[q]:
                color += 1
            
            node2color[nex] = color
            # 辞書に記録
            E[(min(q, nex), max(q, nex))] = color
            queue.append(nex)
        K = max(K, color)
    return K

def main():
    N = int(input())
    G = [deque() for _ in range(N)]
    E = dict() # (a, b) -> color
    for _ in range(N-1):
        a, b = map(lambda x: int(x)-1, input().split())
        G[a].append(b)
        G[b].append(a)
        E[(a, b)] = 0 #辺->色の辞書
    K = bfs(0, N, G, E)
    # ans_list = [value for value in E.values()]
    print(K)
    for value in E.values():
        print(value)
main()