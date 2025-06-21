#6
import sys
H,W = map(int,input().split())
k = H*W

if H ==1 or W == 1:
    print(1)
    sys.exit()

if k%2 == 0:
    print(int(k/2))
else:
    print(int(k/2)+1)