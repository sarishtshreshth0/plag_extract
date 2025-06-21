n = int(input())
a = list(map(int, input().split()))
a.sort()
l = [0]*200000
for i in a:
    if i == 0:
        l[0] += 1
        l[1] += 1
    else:
        l[i-1] += 1
        l[i] += 1
        l[i+1] += 1
print(max(l))