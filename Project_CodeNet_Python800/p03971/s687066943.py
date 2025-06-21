N,A,B = map(int,input().split())
S=input()

passa = 0
passb = 0
for c in S:
    if c == 'a':
        if passa+ passb < A+B:
            print('Yes')
            passa+=1
        else:
            print('No')
    elif c == 'b':
        if passa + passb < A+B and passb < B:
            print('Yes')
            passb+=1
        else:
            print('No')
    else:
        print('No')

