a,b,c=map(int,input().split())
d=input()
total1=0
total2=0
for i in range(a):
    if d[i]=="a":
        if total1+total2<b+c:
            print("Yes")
            total1+=1
        else:
            print("No")
    elif d[i]=="b":
        if total1+total2<b+c and total2<c:
            print("Yes")
            total2+=1
        else:
            print("No")
    else:
        print("No")