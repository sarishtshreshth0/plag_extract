A, B = map(int, input().split(' '))

odd_counts = len([i for i in range(1, 3 + 1) if (A * B * i) % 2 == 1])
if odd_counts > 0:
    print('Yes')
else:
    print('No')
