n, a, b = map(int,input().split())
s = input()

border = a + b
i, j = 1, 1
for p in s:
    flag = False
    if p == "a":
        if i <= a + b:
            flag = True
            i += 1
    elif p == "b":
        if i <= a + b and j <= b:
            flag = True
            i += 1
            j += 1
    if flag:
        print("Yes")
    else:
        print("No")