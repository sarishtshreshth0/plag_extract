n, A, B = map(int, input().split())
a, b = 0, 0
s = input()
for i in range(n):
    s_i = s[i]
    if s_i == 'a':
        if (a + b) < (A + B):
            a += 1
            print('Yes')
        else:
            print('No')
    elif s_i == 'b':
        if ((a + b) < (A + B)) & (b < B):
            b += 1
            print('Yes')
        else:
            print('No')
    else:
        print('No')
    
