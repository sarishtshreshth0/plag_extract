N, A, B = list(map(int, input().split()))
S = input()
AP, BP = 0, 0
for s in S:
    if s == 'a':
        if (AP+BP) < (A+B):
            print('Yes')
            AP += 1
        else:
            print('No')
    elif s == 'b':
        if ((AP+BP) < (A+B)) and (BP < B):
            print('Yes')
            BP += 1
        else:
            print('No')
    else:
        print('No')