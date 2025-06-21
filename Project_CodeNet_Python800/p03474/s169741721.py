import sys

a, b = map(int, input().split())
s = list(input())

for i, j in enumerate(s):
    if i == a:
        if j != '-':
            print('No')
            sys.exit()
    elif j.isdigit():
        continue
    else:
        print('No')
        sys.exit()
print('Yes')

    
