import sys
import math
input=sys.stdin.buffer.readline
h,w=map(int,input().split())
ans=math.ceil(h*w/2)
print(1 if min(h,w)==1 else ans)