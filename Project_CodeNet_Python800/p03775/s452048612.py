N=int(input())
ans=1000000
import math
aa=math.sqrt(N)
aa=int(aa//1)
for A in range(1,aa+1):
    B=N/A
    if B%1.0==0.0:
        ta=len(str(A))
        tb=len(str(int(B)))
        if ta<tb:
            temp=tb
        else:
            temp=ta
        if ans>temp:
            ans=temp

print(ans)
