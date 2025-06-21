a, b = map(int,input().split())
if a == b:
    print('Draw')
elif a == 1:
    print('Alice')
elif b == 1 or b > a:
    print('Bob')
else:
    print('Alice')