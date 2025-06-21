a,b = map(int, input().split())
s = str(input())
num = ['0','1','2','3','4','5','6','7','8','9']
m = 0
for i in range(a+b+1):
    if i == a:
        if s[i] == '-':
            m += 1
    else:
        for h in num:
            if s[i] == h:
                m += 1
if m == a+b+1:
    print('Yes')
else:
    print('No')