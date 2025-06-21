import math
n,d = map(int, input().split())
x = [0] * n
for i in range(n):
    x[i] = list(map(int, input().split()))
count = 0
for i in range(n-1):
    for j in range(i+1,n):
        temp = 0
        for k in range(d):
            temp = temp + (x[i][k]-x[j][k])**2
        temp = math.sqrt(temp)
        if temp.is_integer() == True:
            count += 1
print(count)