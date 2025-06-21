a,b=map(int,input().split())
s=input()
li=["0","1","2","3","4","5","6","7","8","9"]
if s[a]!="-":
    print("No")
    exit()
for i in range(a):
    if not s[i] in li:
        print("No")
        exit()
for i in range(b):
    if not s[-1-i] in li:
        print("No")
        exit()
print("Yes")