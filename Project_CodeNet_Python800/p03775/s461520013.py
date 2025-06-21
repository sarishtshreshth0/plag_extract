from math import sqrt
n = int (input())
nsqrt = int(sqrt(n))
for i in range(nsqrt, 0, -1):
    if n % i == 0:
        b = n // i
        a = i
        break
    if i == 1:
        b = 1
        a = n
def digits(n):
    ans = 0
    while n > 0:
        ans += 1
        n //= 10
    return ans
print (max(digits(a), digits(b)))
                

