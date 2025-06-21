m,d = map(int,input().split())


cnt = 0
for i in range(1,m+1):
    for j in range(1,d+1):
        #print(i,j)
        num = 1
        d2 = (j-j%10)//10
        d1 = j%10
        if d2 >=2 and d1 >=2:
            num =d1*d2
            #print(i,j,num,d1,d2)
        #print(i,j,num,(j-j%10),j%10)
            if num == i:
                cnt +=1
print(cnt)