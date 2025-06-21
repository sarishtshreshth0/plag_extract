def g(N):
    if N%4==0:
        return N
    elif N%4==1:
        return 1
    elif N%4==2:
        return N+1
    else:
        return 0

def f(A,B):
    if A==0:
        return g(B)
    else:
        return g(A-1)^g(B)

A,B=map(int,input().split())
print(f(A,B))