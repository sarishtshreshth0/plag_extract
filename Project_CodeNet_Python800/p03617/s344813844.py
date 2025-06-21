import sys
def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
q, h, s, d = map(int, sys.stdin.readline().rstrip().split())
N = I()
D = d
qh = min(2*q, h)
S = min(2*qh, s)
x = min(2*S, D)
if N%2 == 0:
    print(N//2*x)
else:
    print(N//2*x + S)