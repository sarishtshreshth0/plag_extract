import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    q,h,s,d=map(int, input().split())
    n=int(input())
    s=min(4*q,2*h,s)
    if 2*s<=d:
        print(n*s)
    else:
        a,b=divmod(n,2)
        print(a*d+b*s)
resolve()