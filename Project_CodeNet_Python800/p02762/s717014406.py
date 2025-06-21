import sys
sys.setrecursionlimit(10 ** 6 + 10)

n, m, k = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(m)]
CD = [list(map(int, input().split())) for _ in range(k)]
group = []  # 連結成分ごとのサイズ
person_group = [-1] * n  # 人ごとの属するグループ
person_unable= [0] * n  # 人ごとの候補に入らない人の人数
graph = [[] for _ in range(n)]  # 連結リスト
for ab in AB:
    ab[0] -= 1
    ab[1] -= 1
    graph[ab[0]].append(ab[1])
    graph[ab[1]].append(ab[0])

seen = [False] * n
# その節の連結成分のサイズを返す
def dfs(n, group_id):
    global size
    seen[n] = True
    person_group[n] = group_id
    for v in graph[n]:
        if seen[v]:
            continue
        size = dfs(v, group_id)
    size += 1
    return size
    
    
group_id = 0
for i in range(n):
    if seen[i]:
        continue
    size = 0
    group.append(dfs(i, group_id))
    group_id += 1

# unable計算。まず友達の人
for i in range(n):
    person_unable[i] += len(graph[i])
# 次にブロックの人
for i in range(k):
    CD[i][0] -= 1
    CD[i][1] -= 1
    if person_group[CD[i][0]] == person_group[CD[i][1]]:
        person_unable[CD[i][0]] += 1
        person_unable[CD[i][1]] += 1

for i in range(n):
    print(group[person_group[i]] - person_unable[i] - 1, "", end="")