import fractions
n = int(input())

ans = 2 * n // fractions.gcd(2, n)
print(ans)
