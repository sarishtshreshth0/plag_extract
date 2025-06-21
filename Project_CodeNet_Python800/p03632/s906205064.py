a,b,c,d=map(int,input().split())
if a==c:
    print(min(b,d))
elif a<c:
    if b>d:
        print(d-c)
    else:
        print(max(0,b-c))
else:
    if b<d:
        print(b-a)
    else:
        print(max(0,d-a))