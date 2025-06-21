import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
W = LI()


min_v = 1000000
for t in range(1,N+1):

    a = sum(W[:t])
    b = sum(W[t:])
    min_v = min(min_v,abs(a-b)) 
print(min_v)
