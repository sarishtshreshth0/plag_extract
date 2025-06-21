a,b=map(int,input().split())
x=0
for i in range(3):
    if (a*b*(i+1))%2!=0:
        x+=1
if x>=1:
    print("Yes")
else:
    print("No")