S = list(input())

import numpy as np

S = np.array(S)

zeroichi = ["0","1"]*(len(S)//2)+["0"]*(len(S)%2)
ichizero = ["1","0"]*(len(S)//2)+["1"]*(len(S)%2)

zeroichi = np.array(zeroichi)
ichizero = np.array(ichizero)

print(min(list(S == ichizero).count(False),list(S == zeroichi).count(False)))