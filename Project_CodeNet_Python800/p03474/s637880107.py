# B - Postal Code
A,B = map(int,input().split())
S = input()
if str.isdecimal(S[:A]) and S[A]=='-' and str.isdecimal(S[A+1:]):
    print('Yes')
else:
    print('No')