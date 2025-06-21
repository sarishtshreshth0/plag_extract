A,B = map(int,input().split())
S = input()
S1= S[:A]
S2 = S[A]
S3 = S[A+1:]

if S1.isdecimal() == 1 and S2 == '-' and S3.isdecimal() == 1:
    print('Yes')
else:
    print('No')
