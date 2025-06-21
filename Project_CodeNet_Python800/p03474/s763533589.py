a,b = map(int,input().split())
s = input()
if '-' in s[:a]:
    print('No')
elif s[a] != '-':
    print('No')
elif '-' in s[a+1:]:
    print('No')
else:
    print('Yes')