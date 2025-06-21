Alice,Bob = map(int,input().split())
if Alice == 1:
    Alice = 14
if Bob == 1:
    Bob = 14
if Alice>Bob:
    print('Alice')
elif Alice==Bob:
    print('Draw')
else:
    print('Bob')
