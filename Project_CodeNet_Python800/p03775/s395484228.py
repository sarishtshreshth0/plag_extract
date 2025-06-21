def get_digit(n):
    digit = 0
    while n > 0:
        n //= 10
        digit += 1
    return digit


n = int(input())
a = 1
b = n
res = float('inf')
while a * a <= n:
    if n % a == 0:
        b = n // a
        temp = max(get_digit(a), get_digit(b))
        if temp < res:
            res = temp
    a += 1
print(res)
