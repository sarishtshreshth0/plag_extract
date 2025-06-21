N = list(input())
n = ''.join(N)
N = list(map(int, N))
s = sum(N)
n = int(n)
if n % s == 0:
    print('Yes')
else:
    print('No')