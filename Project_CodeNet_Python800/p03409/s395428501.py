# 解説AC
import sys
input = sys.stdin.readline
n=int(input())
R=[list(map(int,input().split())) for i in range(n)]
B=sorted([tuple(map(int,input().split())) for i in range(n)])
ans=0
for i in range(n):
    a,b=B[i][0],B[i][1]
    y=-1
    ind=-1
    for j in range(n):
        c,d=R[j][0],R[j][1]
        if c<a and d<b and y<d:
            ind=j
            y=d
    if ind>=0:
        ans+=1
        R[ind][0]=1000
        R[ind][1]=1000
print(ans)