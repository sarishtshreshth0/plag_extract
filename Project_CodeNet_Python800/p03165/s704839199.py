# Author: S Mahesh Raju
# Username: maheshraju2020
# Date: 31/07/2020

from sys import stdin,stdout
from math import gcd, ceil, sqrt
from collections import Counter
from bisect import bisect_left, bisect_right
ii1 = lambda: int(stdin.readline().strip())
is1 = lambda: stdin.readline().strip()
iia = lambda: list(map(int, stdin.readline().strip().split()))
isa = lambda: stdin.readline().strip().split()
mod = 1000000007

s, t = is1(), is1()
dp = [[0 for i in range(len(s) + 1)] for j in range(len(t) + 1)]
for i in range(1, len(t) + 1):
    for j in range(1, len(s) + 1):
        if s[j - 1] != t[i - 1]:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        else:
            dp[i][j] = 1 + dp[i - 1][j - 1]

i, j = len(t), len(s)
res = ""
while i > 0 and j > 0:
    if s[j - 1] == t[i - 1]:
        res += s[j - 1]
        i -= 1
        j -= 1
    else:
        if dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:   
            j -= 1
print(res[::-1])
        
    
