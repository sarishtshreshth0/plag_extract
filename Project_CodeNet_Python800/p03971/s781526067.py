n,a,b=map(int,input().split())
s=input()
ans=0
count=0
for i in range(n):
    if s[i]=="c":
        print("No")
        continue
    elif s[i]=="b":
        if count<b and ans<a+b:
            print("Yes")
            ans+=1
            count+=1
        else:
            print("No")
    else:
        if ans<a+b:
            print("Yes")
            ans+=1
        else:
            print("No")