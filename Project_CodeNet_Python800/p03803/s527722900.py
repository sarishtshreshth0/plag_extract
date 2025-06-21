A,B=map(int,input().split())
if A>B:
    if B!=1:
        print('Alice')
    else:
        print('Bob')
elif B>A:
    if A!=1:
        print('Bob')
    else:
        print('Alice')
else:
    print('Draw')