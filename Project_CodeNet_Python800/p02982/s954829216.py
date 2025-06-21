import math

N,D = map(int,input().split())
x = []
count = 0

for i in range(N):
    x.append(list(map(int,input().split())))

for i in range(N):
    for j in range(i+1,N):
        Distance = 0
        for k in range(D):
            Distance += (x[i][k] - x[j][k])**2
        
        if math.sqrt(Distance) == int(math.sqrt(Distance)):
            count += 1
            
print(count)
