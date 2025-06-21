A,B = map(int,input().split())
a = (A-2)%13
b = (B-2)%13

if a==b:
    print('Draw')
elif a>b:
    print('Alice')
else:
    print('Bob')