A, B = map(int, input().split())
S = list(input())

for i in range(len(S)):
    if i <= A-1:
        if S[i] not in [str(i) for i in range(10)]:
            print('No')
            exit()
    if i == A:
        if S[i] != '-':
            print('No')
            exit()
    else:
        if S[i] not in [str(i) for i in range(10)]:
            print('No')
            exit()

print('Yes')