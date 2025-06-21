n,a,b=map(int,input().split())
s=input()
passed=0
abroad_passed=0
for i in s:
    if i=="a":
        if passed<a+b:
            print("Yes")
            passed+=1
        else:
            print("No")
    elif i=="b":
        if passed<a+b and abroad_passed<=b-1:
            print("Yes")
            passed+=1
            abroad_passed+=1
        else:
            print("No")
    else:
        print("No")