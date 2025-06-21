n, k = list(map(int, input().split()))
ans = ''
while n > 0:
    ans = str(n % k) + ans
    n //= k
print(len(ans))