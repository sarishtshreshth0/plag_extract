
N = int(input())

A_start = int(N**0.5)

for A in range(A_start, 0, -1):
    if N % A != 0:
        continue
    B = N // A
    print(len(str(B)))
    break

