def main():
    from sys import setrecursionlimit, stdin, stderr
    from os import environ
    from collections import defaultdict, deque, Counter
    from math import ceil, floor
    from itertools import accumulate, combinations, combinations_with_replacement
    setrecursionlimit(10**6)
    dbg = (lambda *something: stderr.write("\033[92m{}\033[0m".format(str(something)+'\n'))) if 'TERM_PROGRAM' in environ else lambda *x: 0
    input = lambda: stdin.readline().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    P = 10**9+7
    INF = 10**18+10

    N = II()
    A = LMIIS()
    tmp_sum = 0
    num_appeared = defaultdict(int)
    num_appeared[0] = 1

    for a in A:
        tmp_sum += a
        num_appeared[tmp_sum] += 1
    ans = 0

    for v in num_appeared.values():
        ans += v*(v-1)//2


    print(ans)
        


    
main()