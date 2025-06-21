a,b=map(int,input().split())
s=input()
flag=True
for i in range(len(s)):
    if i==a:
        if s[i]!='-':
            flag=False
            break
        continue
    if not(s[i]>='0' and s[i]<='9'):
        flag=False
        break
print("Yes") if flag else print("No")