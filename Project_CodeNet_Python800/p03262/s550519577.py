from functools import reduce
import math
def main():
    n, s = map(int, input().split())
    X = list(map(lambda x:abs(int(x) - s), input().split()))
    ans = reduce(lambda x, y :math.gcd(x, y), X, X[0])
    print(ans)

if __name__ == '__main__':
    main()
