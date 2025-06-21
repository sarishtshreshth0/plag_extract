import math
N,D=map(int,input().split())
cord=[list(map(int,input().split())) for i in range(N)]
ans=0
for i in range(N-1):
    for j in range(i+1,N):
        distance=math.sqrt(sum((cord[i][s]-cord[j][s])**2 for s in range(D)))
        if distance-int(distance)<=0.0001:
            ans+=1

print(ans)