from math import log10
n = int(input())
ans = int(log10(n)) + 1
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        temp = int(log10(n // i)) + 1
        if temp < ans:
            ans = temp
print(ans)