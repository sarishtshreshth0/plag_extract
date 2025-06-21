import fractions
N = int(input())
def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

print(lcm(2, N))