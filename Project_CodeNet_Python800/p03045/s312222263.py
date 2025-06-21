n, m = map(int, input().split())

card = [[] for _ in range(n)]

for _ in range(m):
    x, y, _ = map(int, input().split())
    card[x-1].append(y-1)
    card[y-1].append(x-1)

checked = [False] * n

count = 0
import queue
q = queue.Queue()
for i in range(n):
    if checked[i]:
        continue
    count += 1
    q.put(i)
    while not q.empty():
        j = q.get()
        checked[j] = True
        for k in card[j]:
            if not checked[k]:
                q.put(k)

print (count)


    

