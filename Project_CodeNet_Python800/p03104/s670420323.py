#coding:utf-8
import sys,os
from collections import defaultdict, deque
from math import gcd, ceil, floor
sys.setrecursionlimit(10**6)
write = sys.stdout.write
dbg = (lambda *something: print(*something)) if 'TERM_PROGRAM' in os.environ else lambda *x: 0
def main(given=sys.stdin.readline):
    input = lambda: given().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    MOD = 10**9+7

    A,B = LMIIS()
    if A & 1:
        if B & 1:
            #A, (A+1 A+2).....(B-1,B)
            print(A^(B-A)//2%2)
        else:
            #A, (A+1 A+2).....(B-2,B-1),B
            print(A^((B-A-1)//2%2)^B)
    else:
        if B & 1:
            #(A, A+1).....(B-1,B)
            print((B-A+1)//2%2)
        else:
            #(A, A+1).....(B-2,B-1),B
            print((B-A)//2%2^B)



    

if __name__ == '__main__':
    main()