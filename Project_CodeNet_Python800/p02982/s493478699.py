n,d=map(int,input().split())
x=[list(map(int, input().split())) for i in range(n)]
count=0
ans=0
for i in range(n):
    for z in range(i+1,n):
        for c in range(d):
            ans+=(x[i][c]-x[z][c])**2
        if (ans**0.5)%1==0:
            count+=1
        ans=0
print(count)