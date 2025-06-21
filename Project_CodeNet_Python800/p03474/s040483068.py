a,b = list(map(int, input().strip().split()))
s= input().strip()
f="Yes"
if s[a]!='-':
    f="No"

for i in range(a):
    if  s[i]=="-":
        f="No"
        break

for i in range(a+1,a+b+1):
    if  s[i]=="-":
        f="No"
        break
print(f)