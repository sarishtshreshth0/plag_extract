n,d=map(int,input().split())
li=[list(map(int, input().split())) for _ in range(n)]
res=0
import math
for i in range(n):
    for j in range(i+1,n):
        dis2=0
        for k in range(d):
          dis2+=(li[i][k]-li[j][k])**2
        dis=dis2**(1/2)
        if dis%1==0:res+=1
print(res)