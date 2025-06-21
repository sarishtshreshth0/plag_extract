a, b = map(int, input().split())

if a == 1 and b == 1:
    a = 14
    b = 14
elif a == 1:
    a = 14
elif b == 1:
    b = 14

if a > b:
    print('Alice')
elif a < b:
    print('Bob')
else:
    print('Draw')
