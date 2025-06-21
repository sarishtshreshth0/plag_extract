A, B = map(int, input().split())
S = input()
s = S.replace('-', '')

if len(s) == A + B and S[A] == '-':
    print('Yes')
else:
    print('No')
