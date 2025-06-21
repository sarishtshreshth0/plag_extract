M,D=map(int,input().split())
N=0
if M<4 or D<21:
    print(0)
else: 
    for i in range(1,M+1,1):
        for j in range(1,D+1,1):
            if (j//10)*(j%10)== i and j//10>=2 and j%10>=2:
                N+=1

    print(N)