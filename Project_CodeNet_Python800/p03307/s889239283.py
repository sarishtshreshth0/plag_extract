from fractions import gcd
def lcm(a, b):
    return (a*b) // gcd(a, b) 
n = int(input())
print(lcm(2, n))