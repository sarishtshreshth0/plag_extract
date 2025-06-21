N = int(input())
CSF = [list(map(int, input().split())) for i in range(N-1)]

import math

for i in range(N):
    time = 0
    for csf in CSF[i:]:
        if time <= csf[1]:
            time = csf[1] + csf[0]
        else:
            time = math.ceil((time - csf[1]) / csf[2])*csf[2] + csf[1] + csf[0]
    print(time)