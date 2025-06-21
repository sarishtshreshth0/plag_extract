n,a,b=map(int,input().split())
s=input()
passed=0
oversea=0
yep=False
cnt=0
for i in range(n):
    if s[i]=="c":
        print("No")
    elif s[i]=="a":
        if passed<(a+b):
            print("Yes")
            passed+=1
        else:
            print("No")
    else:
        if oversea<b and passed<(a+b):
            print("Yes")
            passed+=1
            oversea+=1
        else:
            print("No")
#     if passed>=(a+b):
#         yep=True
#         cnt=len(s)-(i+1)
#         break
# if yep:
#     for i in range(cnt):
#         print("No")