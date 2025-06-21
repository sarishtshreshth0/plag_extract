import sys
input = sys.stdin.readline
from collections import *

M, D = map(int, input().split())
ans = 0

for i in range(1, M+1):
    for j in range(10, D+1):
        d0 = int(str(j)[0])
        d1 = int(str(j)[1])
        
        if d0>=2 and d1>=2 and i==d0*d1:
            ans += 1

print(ans)