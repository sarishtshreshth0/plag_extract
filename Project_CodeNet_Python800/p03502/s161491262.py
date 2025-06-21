n = input()
num = sum([int(x) for x in n])

if int(n)%num is 0:
    print('Yes')
else:
    print('No')
