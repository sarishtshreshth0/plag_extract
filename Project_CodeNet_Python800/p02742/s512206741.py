N,M=list(map(int,input().split()))
import math
if N==1 or M==1:
    print(1)
else:
    print(int(math.ceil(N*M/2)))