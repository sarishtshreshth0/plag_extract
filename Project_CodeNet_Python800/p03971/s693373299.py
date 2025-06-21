n, a, b = map(int, input().split())
s = input()

pass_a = 0
pass_b = 0
for c in s:
    if c == 'a':
        if pass_a + pass_b < a + b:
            print('Yes')
            pass_a += 1
        else:
            print('No')
    elif c == 'b':
        if pass_a + pass_b < a + b and pass_b < b:
            print('Yes')
            pass_b += 1
        else:
            print('No')
    else:
        print('No')
