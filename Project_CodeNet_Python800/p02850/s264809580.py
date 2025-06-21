import queue

n = int(input())

e = []
f = [{} for i in range(n)]

for i in range(n-1):
    a,b = map(int, input().split())
    a-=1
    b-=1
    e.append([a,b])
    f[a][b]=0
    f[b][a]=0

k = 0
for i in range(n-1):
    k = max(k,len(f[i]))

q = queue.Queue()
q.put(0)
used = [[0] for i in range(n)]

while not q.empty():
    p = q.get()
    for key,c in f[p].items():
        if c == 0:
            if used[p][-1]<k:
                col = used[p][-1]+1
            else:
                col = 1
            f[p][key] = col
            f[key][p] = col
            used[p].append(col)
            used[key].append(col)
            q.put(key)

print(k)
for a,b in e:
    print(max(f[a][b],f[b][a]))










