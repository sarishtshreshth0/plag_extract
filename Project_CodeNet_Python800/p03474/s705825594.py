A, B = map(int, input().split())
S = input()
for i in range(A):
    if not S[i].isdecimal():
        print('No')
        exit()
if S[A] != '-':
        print('No')
        exit()
for i in range(A+1, A+B+1):
    if not S[i].isdecimal():
        print('No')
        exit()
print('Yes')
