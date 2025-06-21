def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x%y)

def lcm(x, y):
    if x < y:
        z = x
        x = y
        y = z
    return x / gcd(x, y) * y

print(int(lcm(int(input()), 2)))
