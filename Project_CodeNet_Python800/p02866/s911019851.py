import sys
import math
import itertools
import collections
from collections import deque
from collections import defaultdict

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD2 = 998244353
input = lambda: sys.stdin.readline().strip()

NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

def main():
    N = NI()
    D = NLI()
    
    if D[0] != 0:
        print(0)
        sys.exit()
    else:
        Dc = sorted(collections.Counter(D).items())
        
        if Dc[0] != (0,1):
            print(0)
            sys.exit()
        elif Dc[1][0] != 1:
            print(0)
            sys.exit()
        else:
            ans = 1
            for i in range(2,len(Dc)):
                if Dc[i][0] != i:
                    print(0)
                    sys.exit()
                else:
                    ans = (ans * ((Dc[i-1][1] **Dc[i][1]))%MOD2)%MOD2
            print(ans)



if __name__ == '__main__':
    main()