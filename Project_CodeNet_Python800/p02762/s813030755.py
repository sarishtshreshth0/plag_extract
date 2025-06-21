import collections

n, m, k = map(int, input().split())
ab = [[] for i in range(n + 1)]
cd = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    ab[a].append(b)
    ab[b].append(a)
for i in range(k):
    c, d = map(int, input().split())
    cd[c].append(d)
    cd[d].append(c)
flag = [False for i in range(n + 1)]
groups = []
num = 1
while num <= n:
    if flag[num] == True:
        num += 1
        continue
    else:
        temp = set()
        queue = collections.deque([num])
        while queue:
            temp2 = queue.popleft()
            temp |= {temp2}
            flag[temp2] = True
            for i in ab[temp2]:
                if i not in temp:
                    queue.append(i)
        groups.append(temp)
group = [None for i in range(n + 1)]
for i in range(len(groups)):
    for j in groups[i]:
        group[j] = i
for i in range(1, n + 1):
    temp = groups[group[i]]
    temp2 = temp & set(cd[i])
    temp3 = temp & set(ab[i])
    print(len(temp) - 1 - len(temp2) - len(temp3), end = " ")