import math

def gooddistance(l1, l2):
    calc = []
    
    for i in range(len(l1)):
        calc.append((l1[i] - l2[i])**2)

    if math.sqrt(sum(calc)).is_integer():
        return 1
    else:
        return 0

n, d = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
count = 0

for i in range(n):
    for j in range(i+1,n):
       count += gooddistance(lst[i],lst[j])

print(count)
