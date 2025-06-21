
import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    import math
    n=int(input())
    print(2 * n // math.gcd(2, n))
resolve()