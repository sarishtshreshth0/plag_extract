a, b = map(int, input().split())
s = input()

for i in range(a):
    if s[i] == '-':
        print('No')
        exit()

if s[a] != '-':
    print('No')
    exit()

for i in range(a+1, a+b+1):
    if s[i] == '-':
        print('No')
        exit()

print('Yes')
