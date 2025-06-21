N = int(input())
X = N
f = 0

for i in range(len(str(N))):
    f += N % 10
    N = N // 10

if X % f == 0:
    print('Yes')
else:
    print('No')