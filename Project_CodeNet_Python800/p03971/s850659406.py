n,a,b=map(int,input().split())
s=input()
ab=a+b
now=0
nowb=0
for i in range(n):
    if s[i]=="a":
        if now<ab:
            print("Yes")
            now+=1
        else:
            print("No")
    elif s[i]=="b":
        nowb+=1
        if nowb<=b and now<ab:
            print("Yes")
            now+=1
        else:
            print("No")
    else:
        print("No")