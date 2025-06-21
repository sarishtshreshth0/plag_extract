from collections import deque

N, M, K = map(int, input().split())

f = [set() for _ in range(N + 1)]
b = [set() for _ in range(N + 1)]

for _ in range(M):
    f1, f2 = map(int, input().split())
    f[f1].add(f2)
    f[f2].add(f1)

for _ in range(K):
    b1, b2 = map(int, input().split())
    b[b1].add(b2)
    b[b2].add(b1)


dq = deque()
ans = [0] * (N + 1)
visited = [False] * (N + 1)

for i in range(1, N + 1):

    # iを含む連結リストが既に作られている場合はスキップ
    if visited[i]:
        continue

    # setは{}で書く、後で積集合が楽に取れる
    link = {i}
    dq.append(i)
    visited[i] = True

    # DFS
    while dq:
        n = dq.pop()
        # nのフレンド全員について
        for j in f[n]:
            # まだ訪れていないノードの場合
            if not visited[j]:
                link.add(j)
                dq.append(j)
                visited[j] = True

    for user in link:
        # 全体-既にフレンドの人数-ブロックした人数-自分自身
        # set同士で積集合をとる
        ans[user] = len(link) - len(link & f[user]) - len(link & b[user]) - 1

print(*ans[1:])
