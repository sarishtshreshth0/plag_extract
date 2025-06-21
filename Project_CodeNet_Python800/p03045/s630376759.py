N, M = map(int, input().split())
UF = [-1] * (N+1)
def find(x):
    global UF
    if UF[x] == -1:
        return x
    else:
        UF[x] = find(UF[x])
        return UF[x]
def union(x,y):
    global UF
    xx = find(x)
    yy = find(y)
    if UF[x] == UF[y] == -1:
        UF[y] = xx
        return
    elif xx == yy:
        return 
    else:
        UF[yy] = xx
        return 
    
for _ in range(M):
    x, y, z = map(int, input().split())
    union(x,y)
    
print(sum([i < 0 for i in UF[1:]]))