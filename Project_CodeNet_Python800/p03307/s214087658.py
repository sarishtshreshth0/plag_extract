def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a // gcd (a, b) * b

N = int(input())
print(lcm(2, N))
