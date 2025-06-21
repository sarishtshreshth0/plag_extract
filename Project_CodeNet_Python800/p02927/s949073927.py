m,d  =map(int,input().split())
count = 0
for i in range(1,m+1):
    for j in range(d+1):
        if j < 22 or j%10<2:
            continue
        else:
            a = str(j)
            if int(a[0])*int(a[1])==i:
                count += 1
print(count)