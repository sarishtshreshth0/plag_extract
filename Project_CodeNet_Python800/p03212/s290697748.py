N = int(input())

def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

import numpy as np
L = []
for n in range(3, 10):
    for i in range(3**n):
        i3 = Base_10_to_n(i, 3).zfill(n)
        num = ''
        for j in range(n):
            if i3[j] == '0':
                num += '3'
            elif i3[j] == '1':
                num += '5'
            elif i3[j] == '2':
                num += '7'
        if '3' in num and '5' in num and '7' in num:
            L.append(int(num))
L = np.array(L)
#print(L[L<=N])
print(np.count_nonzero(L[L<=N]))
