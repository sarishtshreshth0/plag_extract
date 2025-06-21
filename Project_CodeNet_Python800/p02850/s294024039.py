# 木なので親から繋がっている1辺のみ色が塗られている状態(根に限っては何も塗られていない)

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N-1)]

g = dict()
for i, (a, b) in enumerate(AB):
    a, b = a-1, b-1
    if a not in g:
        g[a] = set()
    if b not in g:
        g[b] = set()
    g[a].add((b, i))
    g[b].add((a, i))

col = [-1]*N
col[0] = -2
e_col = [-1]*(N-1)

q = [0]
while q:
    par = q.pop()
    par_col = col[par]

    c = 0
    for child, e_i in g[par]:
        # print(child, c)
        if col[child] != -1:
            continue
        while c == par_col:
            c += 1
        e_col[e_i] = c
        col[child] = c
        c += 1
        q.append(child)

# print(col)
# print(e_col)

print(max(e_col)+1)
for e_col_i in e_col:
    print(e_col_i+1)