import numpy as np
s = np.array(list(input()))
t = np.array(list(input()))
n = len(s)
m = len(t)
match = s.reshape(-1,1) == t.reshape(1,-1)
lcs = np.zeros((n+1, m+1), dtype='int32')
for i in range(n):
    lcs[i+1,1:] = np.fmax(lcs[i,:-1]+match[i],lcs[i,1:])
    lcs[i+1] = np.maximum.accumulate(lcs[i+1])
l = []
while n > 0 and m > 0:
    if lcs[n, m] == lcs[n-1, m]:
        n-=1
    elif lcs[n, m] == lcs[n, m-1]:
        m-=1
    else:
        l.append(s[n-1])
        n-=1
        m-=1
print(''.join(l[::-1]))
