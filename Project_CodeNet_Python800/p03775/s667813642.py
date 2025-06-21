def div(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

n = int(input())
ans = float("Inf")
lis = div(n)
y = 1
for x in lis:
    z = n//x
    ans = min(ans, max(len(str(z)), len(str(x))))

print(ans)