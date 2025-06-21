p = input().split()
a = int(p[0])
b = int(p[1])

v = input()
s = list(v)

answer = False

for i in range(len(s)):
    q = s[i]
    if i == a:
        if q == '-':
            answer = True
        else:
            answer = False
            break
    else:
        if q == '-':
            answer = False
            break
        else:
            answer = True

if answer:
    print('Yes')
else:
    print('No')