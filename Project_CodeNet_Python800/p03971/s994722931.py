n, a, b = map(int, input().split())
s = input()
cnt = 0
b_cnt = 0
for c in s:
    if c == 'b':
        b_cnt += 1
        if b_cnt <= b and cnt < a+b:
            cnt += 1
            print('Yes')
        else:
            print('No')
    elif c == 'a':
        if cnt < a+b:
            cnt += 1
            print('Yes')
        else:
            print('No')
    else:
        print('No')