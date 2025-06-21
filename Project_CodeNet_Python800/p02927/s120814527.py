m,d = map(int,input().split())
count = 0

for i in range(1,m+1):
    for j in range(10,d+1):
        a = list(str(j))
        if  int(a[0]) >= 2 and int(a[1]) >= 2 and int(a[0]) * int(a[1]) == i:
            count += 1
print(count)