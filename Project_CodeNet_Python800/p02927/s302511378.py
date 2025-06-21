m,d = map(int,input().split())
c= 0
l = []
for i in range(1,m+1):
    for j in range(1,d+1):
        if j%10 <2 or (j-j%10)//10 < 2:
            continue
        else:
            if (j%10)*((j-j%10)//10) == i:
                c = c+1
                l.append([i,j])
            else:
                continue
print(c)