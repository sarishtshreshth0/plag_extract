N=list(map(int, input().split()))
a=N[0]
b=N[1]
c=N[2]
d=N[3]
if a<c:
    if b<=c:
        print(0)
    else:
        if b<=d:
            print(b-c)
        else:
            print(d-c)
else:
    if d<=a:
        print(0)
    else:
        if d<=b:
            print(d-a)
        else:
            print(b-a)    