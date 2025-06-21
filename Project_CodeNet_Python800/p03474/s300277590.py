a, b = map(int, input().split())
s = input()
try:
    A = int(s[:a])
    B = int(s[b:])
    if s[a] == '-':
        print('Yes')
    else:
        print('No')
except:
    print('No')
