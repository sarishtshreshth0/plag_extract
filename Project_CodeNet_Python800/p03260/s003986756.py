x = input()
a = {}
a = [int(i) for i in x.split()]

y = {1, 2, 3}

c = y.difference(a)
a = list(a)

mult = a[0] * a[1]
c = list(c)[0]
flag = False
for i in y:
    if (mult * i) % 2:
        flag = True
if flag:
    print("Yes")
else:
    print("No")
