A,B=map(int,input().split())
S=input()
if (S[:A]+S[-B:]).isdecimal()and S[A]=='-':print('Yes')
else:print('No')