#55
import math
N,D = map(int,input().split())
x = []
dis = []
cnt = 0

for i in range(N):
    x.append(list(map(int,input().split())))
    
for i in range(N-1): 
    for j in range(i+1,N): 
        num = 0
        for m in range(D):
            num += (x[i][m]-x[j][m])*(x[i][m]-x[j][m])
        dis.append(num)
        
for i in dis:
    if int(math.sqrt(i)) == math.sqrt(i):
        cnt += 1
        
print(cnt)