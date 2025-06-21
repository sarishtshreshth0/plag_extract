import collections, math, bisect

local = False
if local:
    file = open("input.txt", "r")
    import time

def inp():
    if local:
        return file.readline().rstrip()
    else:
        return input().rstrip()

def ints():
    return [int(_) for _ in inp().split()]


if local:
    start=time.time()

N,M = ints()

connection = [dict() for i in range(N)]

for i in range(1, M+1):
    x,y,z = ints()

    connection[x-1][y-1] = True
    connection[y-1][x-1] = True

ans = 0
visited = set()

for i in range(N):
    if i in visited:
        continue

    ans+=1
    stck = [i]
    visited.add(i)

    while len(stck)>0:
        vertex = stck.pop(-1)

        for nextVertex in connection[vertex]:
            if nextVertex not in visited:
                visited.add(nextVertex)
                stck.append(nextVertex)

print(ans)


if local:
    fin = (time.time()-start)*1000
    print("{:.2f}".format(fin) + "ms")
