import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
from itertools import accumulate
from collections import Counter
#======================================================#
def main():
    n = II()
    cum = list(accumulate([0]+MII()))
    cnt = [n for n in Counter(cum).values() if n > 1]
    ans = sum([(n*(n-1))//2 for n in cnt])
    print(ans)

if __name__ == '__main__':
    main()