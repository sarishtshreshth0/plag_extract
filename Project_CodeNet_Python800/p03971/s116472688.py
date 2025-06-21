n, a, b = map(int, input().split())
s = input()
ca, cb = 0, 0
for i in s:
    if i == 'c':
        print('No')
    elif i == 'a' and (ca+cb) < (a+b):
        ca += 1
        print('Yes')
    elif (i == 'b' and (ca+cb) < (a+b) and cb < b):
        cb += 1
        print('Yes')
    else:
        print('No')