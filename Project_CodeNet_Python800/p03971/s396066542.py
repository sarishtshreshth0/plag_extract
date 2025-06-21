def resolve():
    '''
    code here
    https://atcoder.jp/contests/code-festival-2016-qualb/tasks/codefestival_2016_qualB_b
    '''
    N, A, B = [int(item) for item in input().split()]
    S = input()
    d = 0
    c = 0
    for i in range(N):
        temp = S[i]
        if temp == 'a':
            if d < A+B:
                d += 1
                print('Yes')
            else:
                print('No')
        elif temp == 'b':
            if d < A+B and c < B:
                c +=1
                d += 1
                print('Yes')
            else:
                print('No')
        else:
            print('No')

if __name__ == "__main__":
    resolve()
