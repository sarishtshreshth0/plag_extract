def resolve():
    N, A, B = list(map(int, input().split()))
    S = str(input())
    num = 0
    foreignnum = 1
    for i in range(N):
        if S[i] == 'a':
            if (num < A + B):
                num += 1
                print('Yes')
            else:
                print('No')

        if S[i] == 'b':
            if (num < A + B) and (foreignnum <= B):
                num += 1
                foreignnum += 1
                print('Yes')
            else:
                print('No')

        if S[i] == 'c':
            print('No')
    return
resolve()
