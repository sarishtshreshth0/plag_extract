N=int(input())
d=[int(s) for s in input().split()]
ans=0
ans_2=sum(d)
ans_li=[]
import math
for i in range(N):
    ans+=d[i]
    ans_2-=d[i]
    ans_li.append(int(math.fabs(ans-ans_2)))
print(min(ans_li))