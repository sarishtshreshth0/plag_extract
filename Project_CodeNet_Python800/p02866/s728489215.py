N = int(input())
D = list(map(int, input().split()))
# N = 4
# D = [0, 3, 2, 1, 2, 2, 1]

from collections import Counter
import sys

C = Counter(D)

if C[0] != 1:
    print(0)
elif D[0] != 0:
    print(0)
else:
    CL = sorted(C.items())
    num_prev = -1
    val_prev = 1
    ans = 1
    for item in CL:
        num = item[0]
        val = item[1]
        if num != num_prev + 1:
            print(0)
            sys.exit()
        else:
            ans *= val_prev**val
            num_prev = num
            val_prev = val
    print(ans%998244353)