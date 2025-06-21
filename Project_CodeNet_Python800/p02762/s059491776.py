n,m,k = map(int,input().split())
A = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    A[a].append(b)
    A[b].append(a)
C = [[] for i in range(n+1)]
for i in range(k):
    c,d = map(int,input().split())
    C[c].append(d)
    C[d].append(c)
from collections import deque
reach = [0]*(n+1)
for i in range(1,n+1):
    if reach[i] != 0:
        pass
    else:
        reach[i] = i
        q = deque([])
        q.append(i)
        while q:
            x = q.popleft()
            for s in A[x]:
                if reach[s] == 0:
                    q.append(s)
                    reach[s] = i
dis_count = [0]*(n+1)
for i,C0 in enumerate(C):
    for CC in C0:
        if reach[CC] == reach[i]:
            dis_count[i] += 1
import collections
D = collections.Counter(reach)
for i in range(1,n+1):
    print(D[reach[i]]-len(A[i])-dis_count[i]-1,end="")
    print(" ",end="")
print("")