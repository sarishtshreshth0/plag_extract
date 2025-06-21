A, B = [int(a) for a in input().split()]
S = input()

for i, c in enumerate(S):
    if i == A:
        if c != '-':
            print('No')
            exit()
    else:
        if c < '0' or '9' < c:
            print('No')
            exit()
print('Yes')