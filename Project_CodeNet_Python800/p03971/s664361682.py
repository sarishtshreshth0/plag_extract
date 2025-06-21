n,a,b=map(int,input().split())
c,d=0,0
s=input()
for i in s:
    f=0
    if i=='a':
        if c<a+b:
            c+=1
            print('Yes')
            f=1
    elif i=='b':
        if c<a+b and d<b:
            c+=1
            d+=1
            print('Yes')
            f=1
    if f==0:
        print('No')