
n, x=  map(int, raw_input().split(' '))
def gcd(a,b): return a if b == 0 else gcd(b, a % b)
print reduce(gcd,map(lambda c: abs(c - x), map(int, raw_input().split(' '))))