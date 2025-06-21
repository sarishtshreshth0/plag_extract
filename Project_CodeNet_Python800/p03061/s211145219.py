import sys,queue,math,copy,itertools,bisect,collections,heapq
from fractions import gcd

def main():
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())

    N = NI()
    A = LI()
    dp = [[0,0] for _ in range(N-1)]
    dp[0] = [A[0],A[1]]
    for i in range(1,N-1):
        dp[i][0] = gcd(dp[i-1][0],A[i])
        dp[i][1] = max(gcd(dp[i-1][0],A[i+1]),gcd(dp[i-1][1],A[i+1]))
    print(max(dp[-1]))

if __name__ == '__main__':
    main()