a, b = list(map(int, input().split()))
s = input()
flag = True
for i in range(a + b + 1):
    try:
        if i < a or i > a:
            if str(int(s[i])) == s[i]:
                pass
            else:
                flag = False
                break
        else:
            if s[i] == '-':
                pass
            else:
                flag = False
                break
    except:
        flag = False
        break
if flag:
    print('Yes')
else:
    print('No')
