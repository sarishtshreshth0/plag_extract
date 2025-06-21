A, B = map(int, input().split())
if A == B:
    print(A)
else:
    K = []
    if A % 2 == 1:
        K.append(A)
        A += 1
    if (B - A) % 2 == 0:
        if ((B - A) // 2) % 2 == 0:
            K.append(B)
        else:
            K.append(1)
            K.append(B)
    else:
        if ((B - A - 1) // 2) % 2 == 0:
            K.append(B-1)
            K.append(B)
        else:
            K.append(1)
            K.append(B-1)
            K.append(B)
    ans = 0
    for i in K:
        ans = (ans ^ i)
    print(ans)