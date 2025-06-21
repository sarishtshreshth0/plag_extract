from sys import stdin

n = int(stdin.readline().rstrip())
import fractions
def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

print(lcm(2,n))