N, A, B = map(int, input().split())
S = input()

cnt_a = 0
cnt_b = 0
for s in S:
    if s == 'c':
        print('No')
    elif s == 'b':
        if (cnt_b < B) and ((cnt_a + cnt_b) < (A + B)):
            print('Yes')
            cnt_b += 1
        else:
            print('No')
    elif s == 'a':
        if (cnt_a + cnt_b) < (A + B):
            cnt_a += 1
            print('Yes')
        else:
            print('No')
