a,b=map(int,input().split())
s=input()
ans="Yes"
for i in range(a+b+1):
    if i<a or i>a:
        if s[i].isdecimal()==False:
            ans="No"
    if i==a:
        if s[i]!="-":
            ans="No"
print(ans)