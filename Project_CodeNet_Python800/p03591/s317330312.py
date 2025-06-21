from sys import stdin
import math
import re
import queue

input = stdin.readline

MOD = 1000000007

def solve():
    S = (input().rstrip())
    if len(S) < 4:
        print("No")
        return
    if(S[:4] == "YAKI"):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()
