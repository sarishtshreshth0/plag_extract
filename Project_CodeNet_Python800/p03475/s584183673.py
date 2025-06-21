from math import ceil
n, *CSF = map(int, open(0).read().split())
A = []
for i in range(0, 3*(n-1), 3):
    t = 0
    for c, s, f in zip(CSF[i::3], CSF[i+1::3], CSF[i+2::3]):
        if t <= s:
            t = s + c
        else:
            t = ceil((t-s) / f) * f + s + c
    A.append(t)
A.append(0)
print(*A, sep='\n')