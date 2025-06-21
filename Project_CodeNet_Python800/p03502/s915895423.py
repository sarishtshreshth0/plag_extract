N = int(input())
origin_N = N
my_sum = 0
while True:
    my_sum += N % 10
    if (N < 10):
        print('Yes' if origin_N % my_sum  == 0 else 'No')
        break
    else:
        N = N // 10