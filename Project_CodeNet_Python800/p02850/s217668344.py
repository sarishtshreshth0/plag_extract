n = int(input())
branch = [[] for _ in range(n)]
a, b, inda, indb = [], [], [], []
for _ in range(n-1):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    branch[i].append(j)
    branch[j].append(i)
    a.append(i)
    b.append(j)
    inda.append(len(branch[i])-1)
    indb.append(len(branch[j])-1)

kind = max([len(i) for i in branch])
print(kind)

# DFS
color = [0 for _ in range(n)]
todo = [0]
color[0] = 1
while len(todo) > 0:
    num = todo.pop(-1)
    col = color[num]
    if col == kind:
        col = 1
    else:
        col = col + 1
    for i in range(len(branch[num])):
        if color[branch[num][i]] == 0:
            color[branch[num][i]] = col
            todo.append(branch[num][i])
            branch[num][i] = -col
            if col == kind:
                col = 1
            else:
                col = col + 1
            

for i in range(n-1):
    if branch[a[i]][inda[i]] < 0:
        print(-branch[a[i]][inda[i]])
    else:
        print(-branch[b[i]][indb[i]])