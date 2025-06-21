import math
N = int(input())

C = [list(map(int,input().split())) for i in range(N-1)]

for i in range(N-1):
    total = 0
    for j in range(i,N-1):
        total = max(math.ceil(total/C[j][2])*C[j][2],C[j][1])
        total += C[j][0]
    print(total)

print(0)