import math
def gooddistance(l1, l2):
    calc = []
    for i in range(len(l1)):
        calc.append((l1[i] - l2[i])**2)

    if math.sqrt(sum(calc)).is_integer():
        return 1
    else:
        return 0

N, D = map(int, input().split())
lis = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(i+1,N):
       cnt += gooddistance(lis[i],lis[j])

print(cnt)