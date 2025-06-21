


N = int(input())
es = [[] for _ in range(N)]
connected = [0] * N
for i in range(N-1):
    a,b = map(int, input().split())
    a,b = a-1, b-1
    connected[a] += 1
    connected[b] += 1
    es[a].append((b, i))
    es[b].append((a, i))


ans = [0] * (N-1)
used = [False] * (N-1)
q = []
q.append((0, 0)) 

while q:
    curr, pc = q.pop()
    nxt_es_color = 1
    for nxt, es_num in es[curr]:
        if used[es_num]:
            continue
        if nxt_es_color == pc:
            nxt_es_color += 1

        ans[es_num] = nxt_es_color
        used[es_num] = True
        q.append((nxt, ans[es_num]))
        nxt_es_color += 1


print(max(connected))
print(*ans, sep="\n")


