a, b = map(int,input().split())
if a == 1:
    if a < b:
        print('Alice')
    else:
        print('Draw')
elif b == 1:
    if a > b:
        print('Bob')
    else:
        print('Draw')
else:
    if a < b:
        print('Bob')
    elif a > b:
        print('Alice')
    else:
        print('Draw')