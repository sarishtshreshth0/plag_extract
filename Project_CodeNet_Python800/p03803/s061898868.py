a, b = map(int, input().split())

if a > b:
    if b == 1:
        print('Bob')
    else:
        print('Alice')
elif a < b:
    if a == 1:
        print('Alice')
    else:
        print('Bob')
else:
    print('Draw')
