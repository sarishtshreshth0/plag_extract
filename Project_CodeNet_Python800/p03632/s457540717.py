a,b,c,d=map(int,input().split())
if a<c:
    if b<c:
        print(0)
    else:
        if b<d:
            print(b-c)
        else:
            print(d-c)
else:
    if a<d:
        if d<b:
            print(d-a)
        else:
            print(b-a)
    else:
        print(0)