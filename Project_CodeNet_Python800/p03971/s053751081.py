N, A, B = map(int, input().split())
S = input()

X, Y = 0, 0
for s in S:
    if s == 'c':
        print('No')

    if s == 'a':
        if X + Y < A + B:
            print('Yes')
            X += 1
        else:
            print('No')

    if s == 'b':
        if X + Y < A + B and Y < B:
            print('Yes')
            Y += 1
        else:
            print('No')
