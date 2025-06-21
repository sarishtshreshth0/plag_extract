a,b,c,d=map(int,input().split())
if b<c or a>d:
    print(0)
else:
    print(min(b-c,d-a,b-a,d-c))
