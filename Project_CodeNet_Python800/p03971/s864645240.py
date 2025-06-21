n,a,b=map(int,input().split())
s=input()
ta=0
tb=0
for i in range(n):
    if s[i]=="c":
        print("No")
    elif s[i]=="a":
        if ta+tb<a+b:
            print("Yes")
            ta+=1
        else:
            print("No")
    elif s[i]=="b":
        if ta+tb<a+b and tb<b:
            print("Yes")
            tb+=1
        else:
            print("No")