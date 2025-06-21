import re
A, B = map(int,input().split())
S = input()

p = f"\d{{{A}}}-\d{{{B}}}"
pattern = re.compile(p)
if pattern.fullmatch(S):
    print('Yes')
else:
    print('No')