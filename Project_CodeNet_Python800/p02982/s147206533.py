import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readlines
from math import sqrt

def isSquare(n):
    m = int(sqrt(n))
    for x in range(m-2, m+2):
        if x**2 == n:
            return True

def getDistance(xi, xj, dimention):
    d = 0
    for i in range(dimention):
        d += (xi[i] - xj[i])**2
    return d

def main():
    lines = input()

    n, d = list(map(int, lines[0].split()))
    x = []
    for i, xi in enumerate(lines[1:]):
        x.append(list(map(int, xi.split())))

    cnt = 0

    for i, xi in enumerate(x):
        for j, xj in enumerate(x[i+1:]):
            dist = getDistance(xi, xj, d)
            if isSquare(dist):
                cnt += 1
    print(cnt)

main()