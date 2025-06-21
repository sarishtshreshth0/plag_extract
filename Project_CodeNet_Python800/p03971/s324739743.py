N, A, B = map(int, input().split())
S = input()

ac_count = 0
ac_b_count = 0
for s in S:
    if ac_count < A + B:
        if s == 'a':
            print('Yes')
            ac_count += 1

        elif s == 'b' and ac_b_count < B:
            print('Yes')
            ac_count += 1
            ac_b_count += 1

        else:
            print('No')
    else:
        print('No')