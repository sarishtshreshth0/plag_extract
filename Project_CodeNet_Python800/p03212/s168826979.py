n = int(input())
lis = ["3","5","7"]
i = 0
while i < 9:
    X = []
    for L in lis:
        if int(L) < 10**(i):
            pass
        else:
            x3 = "".join([L]+["3"])
            X.append(x3)
            x5 = "".join([L]+["5"])
            X.append(x5)
            x7 = "".join([L]+["7"])
            X.append(x7)
    i += 1
    for x in X:
        lis.append(x)
lis2 = []
for A in lis:
    if "3" in A:
        if "5" in A:
            if "7" in A:
                lis2.append(A)
for i in range(len(lis2)):
    lis2[i] = int(lis2[i])
lis2 = sorted(lis2)
ans = 0
for A in lis2:
    if int(A) > n:
        break
    else:
        ans += 1
print(ans)