n=int(input())
s=list(input())
ins=0
app=0
for i in range(n):
    if s[i]=='(':
        app += 1
    else:
        if app>0:
            app -= 1
        else:
            ins += 1
inL=['(']*ins
app=[')']*app
ans=inL+s+app
print(''.join(ans))