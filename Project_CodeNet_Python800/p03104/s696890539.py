A, B = map(int, input().split())
A -= 1
ak, amod = divmod(A, 4)

cum_a = 0
if amod == 0:
    cum_a = A
elif amod == 1:
    cum_a = 1
elif amod == 2:
    cum_a = 4*ak + 3
else:
    cum_a = 0

bk, bmod = divmod(B, 4)
cum_b = 0
if bmod == 0:
    cum_b = B
elif bmod == 1:
    cum_b = 1
elif bmod == 2:
    cum_b = 4*bk + 3
else:
    cum_b = 0

print(cum_a ^ cum_b)