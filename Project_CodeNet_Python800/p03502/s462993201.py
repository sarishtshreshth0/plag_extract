N = int(input())

a = N
c = 0
while a > 0:
    c += a % 10
    a = int(a / 10)
if N % c == 0:
    print('Yes')
else:
    print('No')