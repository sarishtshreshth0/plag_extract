a, b = map(int, input().split())
if a == 1 and b == 1:
    print('Draw')

elif a == 1 and (2 <= b and b <= 13):
    print('Alice')

elif b == 1 and (2 <= a and a <= 13):
    print('Bob')

elif a > b:
    print('Alice')

elif b > a:
    print('Bob')

elif a == b:
    print('Draw')