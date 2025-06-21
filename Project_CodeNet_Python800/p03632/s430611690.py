a,b,c,d=map(int,input().split())
if c>b or a>d:
    print(0)
elif a>=c:
    if b>d:
        print(d-a)
    else:
        print(b-a)
else:
    if b>d:
        print(d-c)
    else:
        print(b-c)