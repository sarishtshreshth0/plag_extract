def resolve():
    a,b=map(int, input().split())
    if a==1 and b!=1:
        print('Alice')
    elif b==1 and a!=1:
        print('Bob')
    else:
        if a<b:
            print('Bob')
        elif a==b:
            print('Draw')
        else:
            print('Alice')

resolve()