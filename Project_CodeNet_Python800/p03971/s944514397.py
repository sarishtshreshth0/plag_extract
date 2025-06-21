N, A, B = map(int, input().split())
S = input()

count_all = 0
count_f = 0
for i in S:
    if i == 'a':
        if count_all < A + B:
            print('Yes')
            count_all += 1
        else:
            print('No')
    elif i == 'b':
        if count_all < A + B and count_f < B:
            print('Yes')
            count_all += 1
            count_f += 1
        else:
            print('No')
    else:
        print('No')