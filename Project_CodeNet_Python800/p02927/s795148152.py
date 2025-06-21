M,D=map(int,input().split())
cnt=0
for i in range(22,D+1):
    if (i%10)*(i//10)<=M and i%10>=2:
        cnt+=1
print(cnt)