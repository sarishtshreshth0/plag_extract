import sys
import math
import itertools
import collections
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()

NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

def main():
    N = NI()
    A = NLI()
    
    cumsum = [0 for _ in range(len(A)+1)] 
    cnt = A[0]
    cumsum[0] = A[0]
    for n in range(1,len(A)):#
        cumsum[n] = cumsum[n-1] + A[n]
        
    cumsum_c = collections.Counter(cumsum)
    
    cumsum_v = list(cumsum_c.values())
    
    # 組み合わせの総数
    def combinations_count(n, r):
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
    
    ans = 0
    
    for i in cumsum_v:
        if not i == 1:
            ans += combinations_count(i, 2)
    print(ans)
    


if __name__ == '__main__':
    main()