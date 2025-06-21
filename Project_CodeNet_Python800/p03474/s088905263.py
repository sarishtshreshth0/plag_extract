a, b = map(int, input().split())
s = str(input())
c = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(len(s)):
    if i + 1 <= a:
        if s[i] not in c:
            print('No')
            exit()
    elif i == a:
        if s[i] != '-':
            print('No')
            exit()
    else:
        if s[i] not in c:
            print('No')
            exit()
print('Yes')