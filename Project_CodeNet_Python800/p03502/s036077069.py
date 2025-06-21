N = input()
sm = sum(map(int, N))
N = int(N)

if N % sm == 0:
    print('Yes')
else:
    print('No')
