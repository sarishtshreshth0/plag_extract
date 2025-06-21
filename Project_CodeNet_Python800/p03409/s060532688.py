import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def S(): return sys.stdin.readline().rstrip()

N = I()
ab = [tuple(int(j) for j in S().split()) for i in range(N)]
cd = [tuple(int(j) for j in S().split()) for i in range(N)]

from operator import itemgetter

ab = sorted(ab,key=itemgetter(1))
cd = sorted(cd,key=itemgetter(0))

ans = 0
for c,d in cd:
    A = []
    for i in range(N):
        if ab[i][0] < c and ab[i][1] < d:
            A.append(ab[i])
    if len(A) == 0:
        continue
    else:
        ans += 1
        for i in range(N):
            if ab[i] == A[-1]:
                ab[i] = (200,200)
                break

print(ans)