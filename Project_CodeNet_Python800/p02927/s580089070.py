from sys import stdin
import math
import re
import queue

input = stdin.readline

MOD = 1000000007
INF = 122337203685477580

def solve():
    M,D = map(int, input().split())
    cnt = 0
    for m in range(1,M+1):
        for d in range(1,D+1):
           if((d%10)*(d//10) == m and d%10 > 1 and d//10 > 1):
               cnt += 1
            #    print(m,d)

    print(cnt) 

if __name__ == '__main__':
    solve()
