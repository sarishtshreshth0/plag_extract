import sys
import collections

input = sys.stdin.readline
MOD = 998244353

def main():
    N = int(input())
    D = list(map(int, input().split()))

    if D[0] != 0:
        print(0)
        return
    
    D.sort()
    Dmax = max(D)
    Ditems = collections.Counter(D).items()
    Dcount = list(zip(*Ditems))

    Dset = set(Dcount[0])
    if Dset != set(range(Dmax+1)):
        print(0)
        return

    if Dcount[1][0] != 1:
        print(0)
        return

    ans = 1
    for i in range(2, Dmax+1):
        ans *= pow(Dcount[1][i-1], Dcount[1][i], MOD)
        ans %= MOD

    print(ans%MOD)

if __name__ == "__main__":
    main()
