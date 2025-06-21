def sum(N):
    sum = 0
    while N > 0:
        sum += N%10
        N = N//10
    return sum

N = int(input())

print('Yes' if N%sum(N) == 0 else 'No')