n, a, b = map(int, input().split())
st = str(input())
bor = a + b

ans = []

pa = 1
fore = 1

for i in st:
    if i == 'a':
        if pa <= bor:
            print('Yes')
            pa += 1
        else:
            print('No')
    elif i == 'b':
        if pa <= bor:
            if fore <= b:
                print('Yes')
                pa += 1
                fore +=1
            else:
                print('No')
        else:
            print('No')
    else:
        print('No')

