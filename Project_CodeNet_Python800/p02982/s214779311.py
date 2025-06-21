# ABC_123_B_Good_Distance.py
from math import sqrt

N, D = list(map(int, input().split()))
x = [list(map(int, input().split())) for _ in range(N)]

ct = 0
# ans=[]
# dis=[]
for i in range(N):
    for j in range(i+1,N):
        sum = 0
        for k in range(D):
            sum += (x[i][k] - x[j][k])**2
        # dis.append((i,j,sum))
        if int(sqrt(sum))**2 == sum:
            ct += 1
            # ans.append((i,j))
print(ct)
# print(dis)
# print(ans)
