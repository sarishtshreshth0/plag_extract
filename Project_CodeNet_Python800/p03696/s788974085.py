def main():
    from sys import setrecursionlimit, stdin
    from os import environ
    from collections import defaultdict, deque, Counter
    from math import ceil, floor
    from itertools import accumulate, combinations, combinations_with_replacement
    setrecursionlimit(10**6)
    dbg = (lambda *something: print(*something)) if 'TERM_PROGRAM' in environ else lambda *x: 0
    input = lambda: stdin.readline().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    P = 10**9+7
    INF = 10**9+10

    N=II()
    S=input()
    p = 0
    num_right_p = 0
    ans = ''
    r = 0
    for s in S:
        if s == '(':
            p += 1
        else:
            if p > 0:
                p -= 1
            else:
                r += 1

    
        ans = '(' * r + S + ')' * p
    print(ans)
            
    

    
main()