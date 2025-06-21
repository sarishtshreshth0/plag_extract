M,D=map(int,input().split())
a=0
for i in range(1,M+1):
    for j in range(11,D+1):
        if i==((j//10)*(j%10)) and j//10>=2 and j%10>=2:
            a+=1
print(a)