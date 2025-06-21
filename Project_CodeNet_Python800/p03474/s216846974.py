import sys
A, B = map(int, input().split())
S = list(input())
for i in range(A):
    if not S[i].isdecimal():
        print('No')
        sys.exit()
if S[A] != '-':
    print('No')
    sys.exit()
for i in range(B):
    if not S[A + 1 + i].isdecimal():
        print('No')
        sys.exit()
print('Yes')