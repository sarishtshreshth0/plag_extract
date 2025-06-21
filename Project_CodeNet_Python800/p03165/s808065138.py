s,t=input(),input()
m,n=len(s),len(t)
c=[[0]*(n+1) for _ in range(m+1)]
fro=[['']*(n+1) for _ in range(m+1)]
for i in range(1,m+1):
    for j in range(1,n+1):
        if s[i-1]==t[j-1]:
            c[i][j]=c[i-1][j-1]+1
            fro[i][j]='upper_left'
        elif c[i-1][j]>=c[i][j-1]:
            c[i][j]=c[i-1][j]
            fro[i][j]='above'
        else:
            c[i][j]=c[i][j-1]
            fro[i][j]='left'
x=''
a,b=m,n
while a>0 and b>0:
    if fro[a][b]=='upper_left':
        x+=s[a-1]
        a-=1;b-=1
    elif fro[a][b]=='above':
        a-=1
    else:
        b-=1
print(x[::-1])