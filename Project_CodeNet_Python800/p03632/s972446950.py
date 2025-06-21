a,b,c,d=map(int,input().split())

if a<=c and b<=d:
    if b-c>0:
        print(b-c)
    else:
        print(0)    
elif a>=c and b>=d:
    if d-a>0:
        print(d-a)
    else:
        print(0)
elif a<=c and b>=d:
    print(d-c)
elif a>=c and b<=d:
    print (b-a)

