a,b=map(int,input().split())
s=input()
Flag=True
for i in range(a+b+1):
    if i==a:
        if s[i]!='-':
            Flag=False
            break
    else:
        if s[i] =='-':
            Flag=False
            break 
if Flag:
    print('Yes')
else:
    print('No')