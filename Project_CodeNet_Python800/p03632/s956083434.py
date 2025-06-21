a,b,c,d=map(int,input().split())
if c<b<=d:
    print(b-max([a,c]))
elif a<d<b:
    print(d-max([a,c]))
else:
    print(0)
