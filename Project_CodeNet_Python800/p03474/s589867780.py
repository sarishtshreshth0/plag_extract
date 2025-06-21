a,b=map(int,input().split())
s=input()
if a+b+1!=int(len(s)):
    print("No")
    exit()
for i in range(int(len(s))):
    if i==a:
        if s[i]!="-":
            print("No")
            exit()
    else:
        if s[i] not in ["0","1","2","3","4","5","6","7","8","9"]:
            print("No")
            exit()
print("Yes")