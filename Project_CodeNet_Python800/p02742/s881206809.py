import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

H,W = MI()

if H == 1 or W == 1:
    print(1)
elif H*W % 2 == 1:
    print((H*W+1)//2)
else:
    print(H*W//2)
