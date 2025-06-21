s = input()
a = 'YAKI'
ans = 0
if len(s) >= 4:
    for i in range(4):
        if s[i] == a[i]:
            ans = 1
        else:
            ans = 0
            break
if ans == 1:
    print('Yes')
else:
    print('No')