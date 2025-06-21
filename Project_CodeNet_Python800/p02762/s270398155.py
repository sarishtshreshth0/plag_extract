from queue import deque

n, m, k = map(int, input().split())

friends = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    friends[a].append(b)
    friends[b].append(a)

checked = [False] * n
groups = []
for i in range(n):
    if checked[i]:
        continue
    checked[i] = True

    que = deque([i])
    group = [i]
    while que:
        now = que.popleft()
        friends_now = friends[now]
        for friend in friends_now:
            if checked[friend] == False:
                checked[friend] = True
                group.append(friend)
                que.append(friend)
    groups.append(group)

# print(groups)

D = dict()
for i in range(len(groups)):
    for j in groups[i]:
        D[j] = i

# print(D)

block = [0] * n
for _ in range(k):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if D[c] == D[d]:
        block[c] += 1
        block[d] += 1

for i in range(n):
    group_i = D[i]
    print(len(groups[group_i]) - block[i] - len(friends[i]) - 1)