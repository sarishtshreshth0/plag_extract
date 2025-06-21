a,b=map(int,input().split())
s=list(input())
num=["0","1","2","3","4","5","6","7","8","9"]
flg=True
for i in range(len(s)):
    if i==a:
        if s[i]!="-":
            flg=False
            break
    else:
        if not(s[i] in num):
            flg=False
            break
if flg:
    print("Yes")
else:
    print("No")