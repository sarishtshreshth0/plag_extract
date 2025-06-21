M,D = list(map(int,input().split()))
count = 0
for i in range(1,M+1):
    for j in range(1,D+1):
        if len(str(j)) == 1:
            continue
        d10 = int(str(j)[0])
        d1 = int(str(j)[1])
        if d10 >= 2 and d1 >= 2 and d10*d1 == i:
            count += 1
print(count)