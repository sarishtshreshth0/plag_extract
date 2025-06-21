a, b, c = map(int, input().split())
a, b = (a, b) if b > a else (b, a)

if a < c and c < b:
    print('Yes')
else:
    print('No')
