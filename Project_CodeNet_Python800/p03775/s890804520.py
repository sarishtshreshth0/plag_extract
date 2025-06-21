N=int(input())
from math import sqrt, log10

def divisor(num):
    max_num = int(sqrt(num))
    divisor_list = []
    for i in range(1, max_num + 1):
        if num % i == 0:
            divisor_list.append(i)
            # divisor_list.append(num//i)
    return divisor_list
ans = float("inf")
for div in divisor(N):
    a = div
    b = N//div
    da = int(log10(a)) + 1
    db = int(log10(b)) + 1
    ans = min(ans, max(da,db))

print(ans)