m,d = map(int,input().split())
c = 0

for i in range(1,m+1):
    for j in range(1,d+1):
        if j >=10:
            tmp = str(j)[0]
            tmp2 = str(j)[1]
            if i == int(tmp) * int(tmp2) and int(tmp) >=2 and int(tmp2) >= 2:
                c += 1
print(c)

