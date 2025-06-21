n = int(input())
arr = []
for i in range(n-1):
    arr.append(tuple(map(int, input().split())))

for i in range(n-1):
    c1, s1, f1 = arr[i]
    ct = s1+c1
    for j in range(i+1, n-1):
        c2, s2, f2 = arr[j]
        while ct > s2:
            s2 += f2
        ct = s2 + c2
    print (ct)
print (0)