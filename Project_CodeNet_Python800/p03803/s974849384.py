a, b = map(int, input().split())
l = [i for i in range(2, 14)] + [1]

if l.index(a) > l.index(b):
    print('Alice')
elif l.index(a) < l.index(b):
    print('Bob')
else:
    print('Draw')
