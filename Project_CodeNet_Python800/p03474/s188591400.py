import re

A,B=map(int,input().split())
S=input()

m = '\d'*A + '-' + '\d'*B

if re.match(m,S):
    print('Yes')
else:
    print('No')