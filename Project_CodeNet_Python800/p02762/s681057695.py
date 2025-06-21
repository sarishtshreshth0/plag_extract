def find(i):
    x = i
    while x!=G[x][0]:
        x = G[x][0]
    return x
def union(i,j):
    ai = find(i)
    ni = G[ai][1]
    aj = find(j)
    nj = G[aj][1]
    if ai!=aj:
        if ni>=nj:
            G[aj][0] = ai
            if G[aj][1]==G[ai][1]:
                G[ai][1] += 1
            G[ai][2] += G[aj][2]
        else:
            G[ai][0] = aj
            G[aj][2] += G[ai][2]
N,M,K = map(int,input().split())
G = {i:[i,0,1] for i in range(1,N+1)}
A = {i:[] for i in range(1,N+1)}
B = {i:[] for i in range(1,N+1)}
for _ in range(M):
    a,b = map(int,input().split())
    union(a,b)
    A[a].append(b)
    A[b].append(a)
for _ in range(K):
    c,d = map(int,input().split())
    B[c].append(d)
    B[d].append(c)
C = []
for i in range(1,N+1):
    ai = find(i)
    n = G[ai][2]
    m = len(A[i])
    k = 0
    for j in B[i]:
        if ai==find(j):
            k += 1
    n = n-m-k
    C.append(n-1)
print(*C)