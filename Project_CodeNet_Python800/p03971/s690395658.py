n,a,b=map(int,input().split())
c=a+b
s=input()
count1=0
count2=0
for i in s:
    if count1>=c:
        print("No")
        continue
    else:
        if i=="a":
            print("Yes")
            count1+=1
            continue
        if i=="b" and count2<b:
            print("Yes")
            count1+=1;count2+=1
            continue
        print("No")
