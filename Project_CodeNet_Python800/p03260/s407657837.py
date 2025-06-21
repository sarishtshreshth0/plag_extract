a,b=map(int,input().split())

flag=False
for c in range(1,4):
    if a*b*c % 2 !=0:
        flag=True
        break

if flag:
    print("Yes")
else:
    print("No")
