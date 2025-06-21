import sys
sys.setrecursionlimit(500000)
N,M,K = map(int, input().split())
V = []

color = [-1]*N
V_block = []

#各連結成分の次元テーブル
dic = {}

dim = 0
#深さ優先探索
def dfs(node, c):
    global dim

    if color[node]!=-1:
        return
    color[node] = c
    dim = dim + 1
    for next_node in V[node]:
        dfs(next_node, c)
    return

for _ in range(N):
    V.append(set())
    V_block.append(set())
for _ in range(M):
    a,b = map(int, input().split())
    V[a-1].add(b-1)
    V[b-1].add(a-1)

#一旦捨てる
for _ in range(K):
    c,d = map(int, input().split())
    V_block[c-1].add(d-1)
    V_block[d-1].add(c-1)
    
c = 0
for node in range(N):
    if color[node]!=-1:
        continue
    dim = 0
    dfs(node, c)
    dic[c] = dim

    c = c + 1

ans_list = []
for node in range(N):
    num = 0
    for block_node in V_block[node]:
        if color[node]==color[block_node]:
            num = num + 1
    ans_list.append(dic[color[node]]-num-len(V[node])-1)

print(*ans_list)

