N = int(input())

nsum = 0
n = N
while n != 0:
    nsum += n % 10
    n = n//10
if N % nsum == 0:
    print('Yes')
else:
    print('No')
