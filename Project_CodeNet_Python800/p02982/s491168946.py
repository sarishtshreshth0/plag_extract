import sys
import itertools
import math
input = lambda: sys.stdin.readline().rstrip()

def main():
    n, d = map(int, input().split())
    x = []
    for _ in range(n):
        x.append(list(map(int, input().split())))
    ans = 0
    for comb in itertools.combinations(range(n), 2):
        dis = 0
        for i, j in zip(x[comb[0]], x[comb[1]]):
            dis += (i - j)**2
        if str(math.sqrt(dis)).split('.')[-1] == '0':
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()