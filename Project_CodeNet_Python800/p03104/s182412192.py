import numpy as np

A, B = map(int, input().split())

# bins = np.array([i for i in range(A, B+1)], dtype='int64')
if A % 2 == 0:
    if B % 2 == 0:
        # 偶偶
        if ((B - A) / 2) % 2 == 0:
            print(int(bin(B ^ 0), 2))
        else:
            print(int(bin(B ^ 1), 2))
    else:
        # 偶奇
        if ((B - A + 1) / 2) % 2 == 0:
            print(0)
        else:
            print(1)
else:
    if B % 2 == 0:
        # 奇遇
        if ((B-A-1) / 2) % 2 == 0:
            print(int(bin(B ^ A), 2))
        else:
            print(int(bin(B ^ A ^ 1), 2))
    else:
        # 奇奇
        if ((B-A) / 2) % 2 == 0:
            print(A)
        else:
            print(A ^ 1)
