A,B = map(int,input().split())
if A==1 and B==1:
    A=14
    B=14
elif A==1 and B!=1:
    A=14
elif B==1 and A!=1:
    B=14
if A>B:
    print('Alice')
elif B>A:
    print('Bob')
elif A==B:
    print('Draw')
