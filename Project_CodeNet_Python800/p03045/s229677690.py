n,m=map(int,input().split())

def find(x):
    if parents[x] < 0: # 負なら根
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]
    
#xとyの属する集合の併合
def unite(x,y):
    x = find(x) # x,yは根の番号にする。
    y = find(y)
    
    if x == y:
        return False
    else:
        if parents[x] > parents[y]: # sizeの大きいほうがx
            x,y = y,x
        parents[x] += parents[y]
        parents[y] = x
        return True

parents=[-1]*n

for i in range(m):
    x,y,z=map(int,input().split())
    unite(x-1,y-1)

ans=0
for i in range(n):
    if parents[i]<0:
        ans+=1
print(ans)