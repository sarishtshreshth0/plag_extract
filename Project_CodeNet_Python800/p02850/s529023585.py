import sys
sys.setrecursionlimit(100000)

n=int(input())

#n番目の頂点が「どの頂点と、何本目の辺つながっているか」をsetの配列で持つ
g = [[] for _ in range(n)]
#i本目の辺(n頂点なのでn-1本ある)が何色か（つまり出力する答え）の配列
ans = [0]*(n-1)

def dfs(target,parent_color,parent):
    next_color = 1

    for a,b in g[target]:
        if target == parent:
            continue
        if next_color == parent_color:
            next_color += 1
        if ans[b] != 0:
            continue
        
        ans[b] = next_color
        next_color += 1
        dfs(a,ans[b],target)
    
for i in range(n-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    g[a].append((b,i))
    g[b].append((a,i))

#print(g)
dfs(0,-1,-1)

print(max(ans))
for a in ans:
    print(a)
