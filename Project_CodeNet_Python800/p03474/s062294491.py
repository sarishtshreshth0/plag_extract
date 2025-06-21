a,b = map(int,input().split())
s = list(input())
for i in range(a+b+1):
    if i < a and not s[i].isdigit():
        print('No')
        exit()
    elif i == a and s[i] != '-':
        print('No')
        exit()
    elif i > a and not s[i].isdigit():
        print('No')
        exit()
print('Yes')