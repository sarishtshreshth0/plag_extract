N,M = (int(X) for X in input().split())
if N>=M:
    print(0)
else:
    P   = sorted(int(X) for X in input().split())
    Mov = sorted([P[X+1]-P[X] for X in range(0,M-1)],reverse=True)
    print(sum(Mov[(N-1):]))