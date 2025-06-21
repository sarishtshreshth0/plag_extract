#B - Postal Code
A,B = map(int,input().split())
S = list(input())

is_A = S[:A]
is_B = S[A+1:A+B+1]
bar = S[A]

if ('-' in is_A) or ('-' in is_B) or bar != '-':
    print('No')
else :
    print('Yes')