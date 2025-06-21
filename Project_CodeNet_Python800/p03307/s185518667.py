def gcd(a, b):   # Greatest Common Divisor
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
def lcm(a, b):   # Least Common Multiple
    return a*b // gcd(a, b)

n = int(input())
print(lcm(2, n))