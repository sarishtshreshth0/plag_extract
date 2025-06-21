N, A, B = map(int, input().split())
S = list(input())

a_pass = 0
b_pass = 0

for s in S:
    if s == 'a':
        if (a_pass + b_pass) < (A + B):
            print('Yes')
            a_pass += 1
        else:
            print('No')
    elif s == 'b':
        if (a_pass + b_pass) < (A + B) and b_pass < B:
            print('Yes')
            b_pass += 1
        else:
            print('No')
    elif s == 'c':
        print('No')