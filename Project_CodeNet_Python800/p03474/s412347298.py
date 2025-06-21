a,b = map(int,input().split())
S = str(input())
if S[a]=='-' and S[:a].isdecimal() and len(S[:a])==a and S[a+1:].isdecimal() and len(S[a+1:])==b:
    print('Yes')
else:
    print('No')