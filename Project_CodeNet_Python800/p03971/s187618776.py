n,a,b=map(int,input().split())
s=input()
passed=0
rank_b=1
for i in range(n):
    if s[i]=="a":
        if passed<a+b:
            print("Yes")
            passed+=1
        else:
            print("No")
    elif s[i]=="b":
        if passed<a+b and rank_b<=b:
            print("Yes")
            rank_b+=1
            passed+=1
        else:
            print("No")
    else:
        print("No")