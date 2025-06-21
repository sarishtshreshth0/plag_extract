a, b, c = map(int,input().split())

if a <= c <= b:
    print('Yes')
    exit()
if b <= c <= a:
    print('Yes')
    exit()
print('No')