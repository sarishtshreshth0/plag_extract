A,B = map(int,input().split())
S = input()
for i in range(A+B+1):
    if i < A and S[i] == '-':
        print('No')
        exit(0)
    elif i == A and S[i] != '-':
        print('No')
        exit(0)
    elif i > A and S[i] == '-':
        print('No')
        exit(0)
print('Yes')