from collections import deque

N = int(input())
# 有向グラフと見る、G[親] = [子1, 子2, ...]
G = [[] for _ in range(N + 1)]
# 子ノードを記録、これで辺の番号を管理
G_order = []
# a<bが保証されている、aを親、bを子とする
for i in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    G[a].append(b)
    G_order.append(b)

# どこでも良いが、ここでは0をrootとする
que = deque([0])

# 各頂点と「親」を結ぶ辺の色
# 頂点0をrootとするのでC[0]=0で確定(「無色」), 他を調べる
colors = [0] * N
# BFS
while que:
    # prt = 親
    # 幅優先探索
    prt = que.popleft()
    color = 0

    # cld = 子
    for cld in G[prt]:
        color += 1
        # 「今考えている頂点とその親を結ぶ辺の色」と同じ色は使えないので次の色にする
        if color == colors[prt]:
            color += 1
        colors[cld] = color
        que.append(cld)

# それぞれの頂点とその親を結ぶ辺の色
# print(colors)

# 必要な最小の色数
print(max(colors))

# 辺の番号順に色を出力
for i in G_order:
    print(colors[i])
