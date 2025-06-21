import math
n,d=map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]
cnt=0
for i in range(0,len(l)-1):
    for j in range(i+1,len(l)):
        sum_num=0
        for k in range(d):
            sum_num+=(l[i][k]-l[j][k])**2
        sum_num=math.sqrt(sum_num)
        if int(sum_num)==sum_num:
            cnt+=1
print(cnt)