n = list(input())
s = sum([int(i) for i in n])

if int(''.join(n))%s == 0:
    print('Yes')
else:
    print('No')