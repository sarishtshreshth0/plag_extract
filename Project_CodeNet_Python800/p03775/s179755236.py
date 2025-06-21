import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())

def make_divisors(n):
    i = 1
    lowest = 10**18
    while i*i <= n:
        if n % i == 0:
            lower_divisor = i
            upper_divisor = n//i
        i += 1
    return len(str(upper_divisor))
    
print(make_divisors(N))