import sys
def input():
    return sys.stdin.readline()[:-1]
inf=float("inf")
x,y=map(int,input().split())
print(x+y//2)