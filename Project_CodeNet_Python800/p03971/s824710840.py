n,a,b = list(map(int,input().split()))
s = list(input())
ok = 0
rank = 1
for i in s:
    if ok >= a+b:
        print('No')
    elif i == 'a':
        print('Yes')
        ok += 1
    elif i == 'b':
        if rank <= b:
            print('Yes')
            rank += 1
            ok += 1
        else:
            print('No')
    else:
        print('No')