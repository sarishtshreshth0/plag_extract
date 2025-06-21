import sys
sys.setrecursionlimit(10**6)
n = int(input())
tree = [[] for i in range(n)]
edge = []

for i in range(n-1):
    a, b = map(int, input().split())
    a-=1; b-=1
    tree[a].append((b, i))
    tree[b].append((a, i))
    edge.append([a, b])

ans = []
def color(a, c=-1, fromnode=None):
    i = 0
    cp = 0
    while i < len(tree[a]):
        nxt, idn = tree[a][i]
        if nxt==fromnode:
            i+=1
            continue 
        if cp == c:
            cp+=1
        ans.append([idn, cp])
        color(nxt, cp, a)
        i+=1
        cp+=1

color(0)

ans.sort()
ans = [c+1 for idn, c in ans]
print(max(ans))
for a in ans:
    print(a)