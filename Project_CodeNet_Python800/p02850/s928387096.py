import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def solve():
    N = int(input())
    adjL = [[] for _ in range(N)]
    for i in range(N-1):
        a, b = map(int, input().split())
        a, b = a-1, b-1
        adjL[a].append((b, i))
        adjL[b].append((a, i))

    def dfs(vNow, vPar, clrPar):
        clr = 1
        for v2, i in adjL[vNow]:
            if v2 == vPar: continue
            if clr == clrPar:
                clr += 1
            anss[i] = clr
            dfs(v2, vNow, clr)
            clr += 1

    anss = [0] * (N-1)
    dfs(0, -1, 0)

    print(max(anss))
    print('\n'.join(map(str, anss)))


solve()
