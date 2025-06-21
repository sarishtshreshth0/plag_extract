A,B = (int(T) for T in input().split())
S = input()
if ('-' not in S[:A]) and (S[A]=='-') and ('-' not in S[(A+1):]):
    print('Yes')
else:
    print('No')