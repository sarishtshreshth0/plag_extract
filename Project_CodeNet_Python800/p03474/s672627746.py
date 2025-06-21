A, B = map(int,input().split())
S = input()
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num = str(num)
if S[A] == '-':
    for i in range(A):
        if S[i] not in num:
            print('No')
            exit()
    for i in range(A + 1, A + B + 1):
        if S[i] not in num:
            print('No')
            exit()
else:
    print('No')
    exit()

print('Yes')