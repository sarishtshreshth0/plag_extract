import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

M, D = mapint()

ans = 0
for m in range(1, M+1):
    for d in range(1, D+1):
        d = str(d)
        if len(d)!=2:
            continue
        d1 = int(d[1])
        d10 = int(d[0])
        if d1<2 or d10<2: continue
        if m==d1*d10:
            ans += 1

print(ans)