def dfs(v, visited):
    """
    :param v: X側の未マッチングの頂点の1つ
    :param visited: 空のsetを渡す（外部からの呼び出し時）
    :return: 増大路が見つかればTrue
    """
    for u in edges[v]:
        if u in visited:
            continue
        visited.add(u)
        if matched[u] == -1 or dfs(matched[u], visited):
            matched[u] = v
            return True
    return False


n = int(input())
r_ls = []
b_ls = []

for i in range(n):
    a, b = map(int, input().split())
    r_ls.append((a, b))

for i in range(n):
    c, d = map(int, input().split())
    b_ls.append((c, d))

edges = [set() for _ in range(n)]
matched = [-1] * n

for i in range(len(r_ls)):
    for j in range(len(b_ls)):
        if r_ls[i][0] < b_ls[j][0] and r_ls[i][1] < b_ls[j][1]:
            edges[i].add(j)

print(sum(dfs(s, set()) for s in range(n)))
