N = input()
f_X = 0
for c in N:
    f_X += int(c)
if int(N) % f_X == 0:
    print('Yes')
else:
    print('No')
