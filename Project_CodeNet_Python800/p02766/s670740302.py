import sys
import math
n,k=map(int,input().split())

p=int(math.log2(n))

for i in range(p+2):
    if n//(k**i)<1:
        print(i)
        sys.exit()