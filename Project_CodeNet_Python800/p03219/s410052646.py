import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    x,y=map(int, input().split())
    print(x+y//2)

resolve()