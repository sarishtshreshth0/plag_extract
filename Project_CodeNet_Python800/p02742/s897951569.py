import math
n,w=map(int,input().split())
if n==1 or w==1:
    print(1)
else:
    ans=math.ceil(w/2)*math.ceil(n/2)+(w//2)*(n//2)
    print(ans)