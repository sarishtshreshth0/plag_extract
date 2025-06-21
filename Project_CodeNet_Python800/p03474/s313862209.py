a, b = map(int, input().split())
s = input()
flg = 0
for i in range(a +b +1):
    try:
        if (0 <= int(s[i]) <= 9):
            if i == a:
                flg = 0
                break
    except:
        if i == a:
            flg = 1
        else:
            flg = 0
            break
print("Yes" if flg == 1 else "No")