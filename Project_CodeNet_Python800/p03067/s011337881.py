a, b, c = (int(i) for i in input().split())  



if a < b:
    if a < c and c < b:
        print('Yes')
    else:
        print('No')

elif a > b:
    if b < c and c < a:
        print('Yes')
    else:
        print('No')