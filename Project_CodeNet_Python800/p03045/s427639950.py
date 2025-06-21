import queue
n, m = map(int,input().split())

pr = [[] for i in range(n+1)]

for i in range(m):
    x,y,z = map(int,input().split())
    pr[x].append(y)
    pr[y].append(x)

def grouping(n,arr):
    gr = []
    al = [-1 for i in range(n+1)]
    q = queue.Queue()
    for i in range(1,n+1):
        if al[i] == 0:
            continue
        else:
            gi = []
            q.put(i)
            al[i] = 0
            while not q.empty():
                qi = q.get()
                gi.append(qi)
                for ai in arr[qi]:
                    if al[ai] < 0:
                        q.put(ai)
                        al[ai] = 0
            gr.append(gi)
    return gr

print(len(grouping(n,pr)))
