from collections import deque

n, m, k = map(int,input().split())

friend_sum = [[] for i in range(n)]
block = []
block_sum = [[] for i in range(n)]

for i in range(m):
    a, b = map(int,input().split())
    if a > b:
        a, b = b, a
    friend_sum[a-1].append(b-1)
    friend_sum[b-1].append(a-1)

for i in range(k):
    a, b = map(int,input().split())
    block.append([a, b])
    block_sum[a-1].append(b-1)
    block_sum[b-1].append(a-1)

label = 0
g_label = [0 for i in range(n)]
g_list = [0 for i in range(n)]

for i in range(n):
    if g_label[i] == 0:
        label += 1
        g_label[i] = label
        g_list[label-1] += 1
        q = deque([])
        q.append(i)
        while len(q) != 0:
            num = q.popleft()
            for j in range(len(friend_sum[num])):
                if g_label[friend_sum[num][j]] == 0:
                    g_label[friend_sum[num][j]] = label
                    g_list[label-1] += 1
                    q.append(friend_sum[num][j])

ans = 0

for i in range(n):
    ans = g_list[g_label[i]-1] - len(friend_sum[i]) - 1
    for j in range(len(block_sum[i])):
        if g_label[i] == g_label[block_sum[i][j]]:
            ans -= 1
    print(ans, end=' ')

print()
