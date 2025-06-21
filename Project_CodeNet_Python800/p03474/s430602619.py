from collections import Counter
a,b = map(int,input().split())
s = input()

if s[a]=='-' and '-' not in s[0:a] and '-' not in s[a+1:]:
    print('Yes')
else:
    print('No')