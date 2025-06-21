import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
import itertools as it
from collections import Counter
#======================================================#
def main():
    n = II()
    aa = MII()
    cum = list(it.accumulate([0]+aa))
    c = Counter(cum)
    cnt = [n for n in c.values() if n > 1]
    ans = sum([(n*(n-1))//2 for n in cnt])
    print(ans)

if __name__ == '__main__':
    main()