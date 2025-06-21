a, b = map(int, input().split())
s = input()

if s[a] != '-':
    print('No')
    exit()
try:
    int(s[:a])
    int(s[a + 1:])
except:
    print('No')
    exit()
print('Yes')