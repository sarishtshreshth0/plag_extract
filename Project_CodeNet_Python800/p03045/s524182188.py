def find(x):
    while x!=T[x][0]:
        x = T[x][0]
    return x
def union(x,y):
    a = find(x)
    b = find(y)
    if T[a][1]>T[b][1]:
        T[b][0] = a
    elif T[a][1]==T[b][1]:
        T[b][0] = a
        T[a][1] += 1
    else:
        T[a][0] = b
N,M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(M)]
T = {i:[i,1] for i in range(1,N+1)}
for j in range(M):
    x,y,z = A[j]
    a = find(x)
    b = find(y)
    if a!=b:
        union(a,b)
C = [0 for _ in range(N+1)]
for i in range(1,N+1):
    a = find(i)
    if C[a]==0:
        C[a] = 1
print(sum(C))