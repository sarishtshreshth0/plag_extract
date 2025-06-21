n = int(input())
a = list(map(int,input().split()))

point = [0]*(10**5+2)

for i in a:
    if i == 1:
        point[1] += 1
        point[2] += 1
    else:
        point[i] += 1
        point[i-1] += 1
        point[i+1] += 1

print(max(point))