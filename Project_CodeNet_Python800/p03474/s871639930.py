def resolve():
    '''
    code here
    '''
    A, B = [int(item) for item in input().split()]
    S = input()

    if S[A] == '-' and len(S) >= 3:
        if '-' in S[:A] or '-' in S[-1*B:]:
            print('No')
        else:
            print('Yes')
    else:
        print('No')
if __name__ == "__main__":
    resolve()
