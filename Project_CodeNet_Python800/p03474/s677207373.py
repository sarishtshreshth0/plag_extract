a, b = map(int, input().split())
s = input()

f = True
if s[a]!='-':
    f = False
if not s[:a].isnumeric() and s[a+1:].isnumeric():
    f = False
if '-' in s[:a]+s[a+1:]:
    f = False
if f:
    print('Yes')
else:
    print('No')