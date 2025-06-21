import numpy as np

S = np.array(list(input()))
S = S.astype('int32')
length = len(S)

if length == 1:
    print(0)
    exit()

check_array1 = np.zeros(length, int)
for i in range(1, length, 2):
    check_array1[i] = 1

check_array2 = np.append(check_array1[1:], check_array1[-2])


checked1_S = S + check_array1
checked2_S = S + check_array2

checked1_total = (checked1_S == 1).sum()
checked2_total = (checked2_S == 1).sum()

answer = min(checked1_total, checked2_total)

print(answer)
