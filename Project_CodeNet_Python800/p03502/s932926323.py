def split_sum(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans


N = int(input())
print('Yes' if N % split_sum(N) == 0 else 'No')
