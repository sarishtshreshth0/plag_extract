a, b = map(int, input().split())
def conv(k):
    if k == 1:
        return k+1000
    else:
        return k
if conv(a) > conv(b):
    print('Alice')
elif conv(a) < conv(b):
    print('Bob')
else:
    print('Draw')