x = int(input())
n = x
m = 0

while n > 0:
    m = m + n % 10
    n = n // 10

if x % m == 0:
    print('Yes')
else:
    print('No')