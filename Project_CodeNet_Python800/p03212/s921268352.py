import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
idx = 0

ans = 0
def dfs(idx, st):
    global ans
    if idx==10:
        return
    if int(st)>N:
        return
    elif len(set(st))>=3:
        ans += 1
    for nx in ('3', '5', '7'):
        dfs(idx+1, st+nx)

for nx in ('3', '5', '7'):
    dfs(1, nx)
print(ans)