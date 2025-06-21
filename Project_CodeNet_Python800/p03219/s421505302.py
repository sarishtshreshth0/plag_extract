import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

X,Y = MI()
print(X + Y//2)
