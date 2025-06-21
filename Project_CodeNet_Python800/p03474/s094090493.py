a, b = map(int, input().split())
s = input()

if len(s) != a + b + 1:
    print('No')
elif s[a] != '-':
    print('No')
elif s[0:a].isdecimal() == False:
    print('No')
elif s[(a + 1):].isdecimal() == False:
    print('No')
else:
    print('Yes')
