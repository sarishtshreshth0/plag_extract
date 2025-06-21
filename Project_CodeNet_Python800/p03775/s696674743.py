N = int(input())
import math
if N == 1:
    print(1)
else:
    for a in reversed(range(1, (int(math.sqrt(N)))+1)):
        if N % a == 0:
            b = N/a
            ans=max(len(str(int(a))), len(str(int(b))))
            break
    print(ans)

