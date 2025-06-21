a, b = map(int, input().split())
if a == 1 and b == 1:
    print('Draw')
else:
    if a == 1:
        print('Alice')
    elif b == 1:
        print('Bob')
    else:
        if a == b:
            print('Draw')
        elif a < b:
            print('Bob')
        else:
            print('Alice')
