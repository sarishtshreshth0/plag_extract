n, a, b = map(int, input().split())
s = input()
c = a+b

for x in s:
    if x == 'a' and c > 0:
        c -= 1
        print('Yes')
    elif x == 'b' and b > 0 and c > 0:
        b -= 1
        c -= 1
        print('Yes')
    else:
        print('No')