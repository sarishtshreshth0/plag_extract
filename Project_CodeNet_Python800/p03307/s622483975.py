import fractions

N = int(input())

print(N*2//fractions.gcd(2, N))
