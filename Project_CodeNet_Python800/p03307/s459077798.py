import fractions
N = int(input())
def lcm(A, B):
    return int((A * B) / fractions.gcd(A, B))
print(lcm(2, N))