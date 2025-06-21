import math
n, d = map(int, input().split())
x = [list(map(int, input().split())) for i in range(n)]
cnt = 0

def distance(list1, list2) :
    dist = 0
    for i in range(len(list1)) :
        dist += (list1[i] - list2[i]) ** 2
    return math.sqrt(dist)

for i in range(n) :
    for j in range(i+1,n) :
        if i != j :
            if int(distance(x[i], x[j])) == distance(x[i], x[j]) :
                cnt += 1
print(cnt)
