import sys
A,B = map(int,input().split())
S = input()
array_S = list(S)

if not (1 <= A <= 5 and 1 <= B <= 5):
    sys.exit()

if len(S) != (A + B + 1):
    sys.exit()

for I in range(len(array_S)):
    if I == A:
        continue
    if not array_S[I].isdecimal():
        print('No')
        sys.exit()

if array_S[A] == '-' and len(S) == (A + B + 1):
    print('Yes')
else:
    print('No')