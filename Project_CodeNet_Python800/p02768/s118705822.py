#coding:utf-8
import sys,os
sys.setrecursionlimit(10**6)
write = sys.stdout.write
dbg = (lambda *something: print(*something)) if 'TERM_PROGRAM' in os.environ else lambda *x: 0
def main(given=sys.stdin.readline):
    input = lambda: given().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    XLMIIS = lambda x: [LMIIS() for _ in range(x)]
    YN = lambda c : print('Yes') if c else print('No')
    MOD = 10**9+7

    n,a,b = LMIIS()
    def cmb(n,r):
        if r == 0:
            return 0
        res = 1
        r = min(r,n-r)
        for i in range(n-r+1,n+1):
            res *= i
            res %= MOD
        for i in range(1,r+1):
            res *= pow(i,(MOD-2),MOD)
            res %= MOD
        return res
    print((pow(2,n,MOD)-cmb(n,a)-cmb(n,b)-1)%MOD)

    
if __name__ == '__main__':
    main()