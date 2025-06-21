import numpy as np
N,D = list(map(int,input().split()))
 
lis =[list(map(int,input().split())) for i in range(N)]
lis_np = np.array(lis)
counter = 0
for i in range(N-1):
    for j in range(i+1,N):
        kyori = (sum((lis_np[:][i] - lis_np[:][j])**2))**0.5
        if kyori == int(kyori):
            counter += 1
        
print(counter)
