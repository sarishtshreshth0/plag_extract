import sys
sys.setrecursionlimit(10**6)

def dfs(GF,group,gn,i):
    size = 1
    group[i]=gn
    for node in GF[i]:
        if group[node]==-1:
            group[node]=gn
            size+=dfs(GF,group,gn,node)
    return size

def main():
    from sys import stdin
    n,m,k = map(int,stdin.readline().rstrip().split())
    F=[]
    for _ in range(m):
        F.append(list(map(int,stdin.readline().rstrip().split())))
    GF = [[] for _ in range(n+1)]
    for a,b in F:
        GF[a].append(b)
        GF[b].append(a)
    
    B=[]
    for _ in range(k):
        B.append(list(map(int,stdin.readline().rstrip().split())))
    GB = [[] for _ in range(n+1)]
    for a,b in B:
        GB[a].append(b)
        GB[b].append(a)    

    U = []
    group= [-1]*(n+1)
    gn = 0

    for i in range(1,n+1):
        if group[i] == -1:
            sz = dfs(GF,group,gn,i)
            gn+=1
            U.append(sz)
    
    for i in range(1,n+1):
        g = group[i]
        ans = U[g]-1-len(GF[i])

        for b in GB[i]:
            if group[b]==g:
                ans-=1
        print(ans,end=" ")
main()