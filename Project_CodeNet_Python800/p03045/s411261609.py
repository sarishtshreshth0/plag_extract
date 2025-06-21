def find(x):
    while x!=T[x][0]:
        x = T[x][0]
    return x
def union(x,y):
    ax = find(x)
    ay = find(y)
    if T[ax][1]>T[ay][1]:
        T[ay][0] = ax
    elif T[ax][1]==T[ay][1]:
        T[ay][0] = ax
        T[ax][1] += 1
    else:
        T[ax][0] = ay
N,M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(M)]
T = {i:[i,1] for i in range(1,N+1)}
for j in range(M):
    x,y = A[j][0],A[j][1]
    union(x,y)
B = [0 for _ in range(N+1)]
for i in range(1,N+1):
    B[i] = find(i)
C = {}
for i in range(1,N+1):
    b = B[i]
    if b not in C:
        C[b] = 0
    C[b] += 1
print(len(C))