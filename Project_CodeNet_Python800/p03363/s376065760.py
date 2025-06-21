import numpy as np
N = int(input())
num = list(map(int, input().split()))

sumz = np.zeros(N+1, dtype=int)
count = np.zeros(N+1, dtype=int)
for i in range(1, N+1):
    sumz[i] = sumz[i-1] + num[i-1]

sortedsumz = np.sort(sumz)

def CC(a, b):
    ans = 1
    mulz = 1
    for i in range(b-a+1, b+1):
        ans *= i
    for i in range(1,a+1):
        mulz *= i
    return int(ans/mulz)

ways = 0
for i in range(1, N+1):
    if sortedsumz[i] == sortedsumz[i-1]:
        count[i] = count[i-1]+1
    elif count[i-1] >= 1:
        ways += CC(2, count[i-1]+1)

    #if sortedsumz[i-1] == 0:
    #    nzero += 1

if count[N] >= 1:
    ways += CC(2, count[N] + 1)
print(ways)
