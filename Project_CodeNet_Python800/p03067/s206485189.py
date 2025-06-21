a,b,c = map(int,input().split())
if a > b:
    z = a
    a = b
    b = z
if a <= c <= b:
    print('Yes')
else:
    print('No')