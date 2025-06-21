b = list(map(int, input().split()))
if b[0]==1 or b[0]==3:
    if b[1]==1 or b[1]==3:
        print('Yes')
    else:
        print('No')
else:
    print('No')