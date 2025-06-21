from collections import deque

N = int(input())
G = [[] for _ in range(N + 1)]
# 辺の色を具体的に出力する際、辺の順番が必要になるので記録しておく
edge_order = []
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
    edge_order.append((a, b))

# どこでも良いが、ここでは1をrootとする
dq = deque([1])

# 辺の色
edge_color = {}
# 子要素を見ていく際、親が既に使った１色だけは使えない、そのチェック
used_color = [0 for _ in range(N + 1)]
# BFSで既に見たかどうか
visited = [False for _ in range(N + 1)]
visited[1] = True

# BFS
while dq:
    # prt = 親
    prt = dq.popleft()
    color = 0

    # cld = 子
    for cld in G[prt]:
        if visited[cld] == False:
            # 訪れたことを記録
            visited[cld] = True
            # 色を決める
            color += 1
            # 親が既に使った色だったらスキップ
            if color == used_color[prt]:
                color += 1

            # この段階で色は確定している

            # 「既に使った色」として記録
            used_color[cld] = color
            # 辺の色を記録
            n1 = min(cld, prt)
            n2 = max(cld, prt)
            edge_color[(n1, n2)] = color
            # キューに追加
            dq.append(cld)

# 使用する色の数
print(max(edge_color.values()))
# 具体的な辺の色を出力
for edge in edge_order:
    print(edge_color[edge])
