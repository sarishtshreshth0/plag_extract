A, B, C, D = map(int, input().split())

M1 = max(A, C)
M2 = min(B, D)

M = M2 - M1

if M > 0:
    print(M)

else:
    print(0)
