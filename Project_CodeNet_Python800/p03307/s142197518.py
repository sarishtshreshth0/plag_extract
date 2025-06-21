import math

def lcm_base(x,y):
    return (x * y) // math.gcd(x,y)

print(lcm_base(2,int(input())))