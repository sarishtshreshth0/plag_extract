from math import log10

N = int(input())

ans = int(log10(N)) + 1

for i in range(2, int(N ** 0.5) + 1):
    if N % i == 0:
        tmp = int(log10(N // i)) + 1
        if tmp < ans:
            ans = tmp

print(ans)