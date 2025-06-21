m, d = map(int,input().split())
cnt = 0
if 20<=d:
    for i in range(20,d+1):
        if (i%10)*(i//10)<=m and 2<=i%10:
            cnt+=1
print(cnt)