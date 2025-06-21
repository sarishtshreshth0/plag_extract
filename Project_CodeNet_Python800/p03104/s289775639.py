


A,B = map(int, input().split())


if A == B:
    print(B)
    exit()
elif B - A == 1:
    print(A ^ B)
    exit()

"""
1 xor 1 = 0
0 xor AAA = AAA
(2*n) xor ((2*n)+1) = 1

とか。

"""
if A % 2 == 0:
    if B % 2 == 1:
        cnt_1 = (B - A + 1) // 2
        if cnt_1 % 2 == 0:
            ans = 0
        else:
            ans = 1
    else:
        cnt_1 = (B-1 - A + 1) // 2
        if cnt_1 % 2 == 0:
            ans = B
        else:
            ans = 1 ^ B
else:
    if B % 2 == 1:
        cnt_1 = (B - (A+1) + 1) // 2
        if cnt_1 % 2 == 0:
            ans = A
        else:
            ans = 1 ^ A
    else:
        cnt_1 = (B-1 - (A+1) + 1) // 2
        if cnt_1 % 2 == 0:
            ans = A ^ B
        else:
            ans = A ^ 1 ^ B
print(ans)