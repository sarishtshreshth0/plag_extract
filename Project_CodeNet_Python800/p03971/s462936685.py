N, A, B = list(map(int, input().split()))
S = input()

total, kaigai = 0, 0

for i in range(N):
    if S[i] == 'c':
        print('No')

    elif S[i] == 'b':
        if total < A+B and kaigai < B:
            print('Yes')
            total += 1
            kaigai += 1
        else:
            print('No')

    elif S[i] == 'a':
        if total < A+B:
            print('Yes')
            total += 1
        else:
            print('No')
