n, a, b = map(int, input().split())
S = list(input())

t_pass = 0
f_pass = 1

for e in S:
    if e == 'a':
        if t_pass < a + b:
            t_pass += 1
            print('Yes')
        else:
            print('No')
    elif e == 'b':
        if t_pass < a + b and f_pass <= b:
            t_pass += 1
            f_pass += 1
            print('Yes')
        else:
            print('No')
    else:
        print('No')
