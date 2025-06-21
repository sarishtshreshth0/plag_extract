a,b=map(int,input().split())
c=1
while True:
    if a*b*c%2!=0:
        print("Yes")
        exit()
    elif c>3:
        break
    elif a*b*c%2==0:
        c+=1 
print("No")