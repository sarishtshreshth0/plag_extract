M,D=map(int,input().split())
cnt=0
for i in range(M):
    for j in range(D):
        a1=(j+1)//10
        a2=(j+1)%10
        if (a1>=2)and(a2>=2)and(a1*a2==(i+1)):
            cnt=cnt+1
print(cnt)