from collections import deque
N, M, K = map(int, input().split())
F = [[] for _ in range(N)]
B = [[] for _ in range(N)]

# フレンドの隣接リスト
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    F[a].append(b)
    F[b].append(a)

# ブロックの隣接リスト
for _ in range(K):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    B[c].append(d)
    B[d].append(c)


# 交友関係グループ（辞書型）
D = {}
# グループの親
parent = [-1] * N
# 訪問管理
visited = [False] * N

for root in range(N):
    cnt = 0
    if visited[root]:
        continue

    # D[root] = set([root])
    # 訪問先のスタック
    stack = [root]
    # 訪問先が無くなるまで
    while stack:
        # 訪問者をポップアップ
        n = stack.pop()
        # 訪問者を訪問済み
        if visited[n]:
            continue
        visited[n] = True
        cnt +=1
        # 訪問者のグループの親を設定
        parent[n] = root

        # root のフレンドをグループと訪問先に追加
        for to in F[n]:
            if visited[to]:
                continue
            # D[root].add(to)
            stack.append(to)
    if cnt!=0:
        D[root]=cnt
# print(D)
ans = [0]*N
for iam in range(N):
    # group = gro[parent[iam]]
    tmp_ans = D[parent[iam]]
    tmp_ans -=1
    tmp_ans -= len(F[iam])
    for block in B[iam]:
        if parent[block]==parent[iam] :
            tmp_ans -=1
    ans[iam]=tmp_ans
print(*ans, sep=' ')