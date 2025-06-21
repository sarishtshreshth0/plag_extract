
# gcdは最大公約数
from fractions import gcd
# lcmは最小公倍数
def lcm(x, y):
    return (x * y) // gcd(x, y)

def main():
    from sys import stdin, setrecursionlimit
    setrecursionlimit(10**6)
    r = stdin.readline()[:-1]
    #n = int(stdin.readline()[:-1])   
    #r = [stdin.readline() for i in range(n)]
    #t = [int(stdin.readline()) for i in range(n)]

    a = int(r)
    print(lcm(2,a))
if __name__ == '__main__':
    main()

