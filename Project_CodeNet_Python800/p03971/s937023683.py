n,a,b=map(int,input().split())
s=input()
counta=0
countb=0
for i in range(n):
    if s[i]=="c":
        print("No")
    elif s[i]=="b":
        if counta<a+b and countb<b:
            counta+=1
            countb+=1
            print("Yes")
        else:
            print("No")
    else:
        if counta<a+b:
            counta+=1
            print("Yes")
        else:
            print("No")
