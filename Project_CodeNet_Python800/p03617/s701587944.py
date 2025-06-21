import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
Q,H,S,D = LI()
N = I()
min_1 = min(Q*4,H*2,S)
if 2*min_1<=D:
    ans = min_1*N
else:
    ans = N//2*D+(min_1 if N%2==1 else 0)
print(ans)
