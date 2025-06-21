from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
from fractions import gcd
from itertools import combinations # (string,3) 3回
from collections import deque
from collections import defaultdict
import bisect
#
#    d = m - k[i] - k[j]
#    if kk[bisect.bisect_right(kk,d) - 1] == d:
#
#
#
# pythonで無理なときは、pypyでやると正解するかも！！
#
#

import sys
sys.setrecursionlimit(10000000)
#mod = 10**9 + 7
mod = 998244353
def readInts():
  return list(map(int,input().split()))
def I():
  return int(input())
flag = False
n = I()
D = readInts()
dic = defaultdict(int)
for i in range(n):
    dic[D[i]] += 1
# 後ろから見る
for i in range(n-1,0,-1):
    if dic[i] != 0:
        flag = True
    if flag and dic[i] == 0:
        print(0)
        exit()
if dic[0] != 1: # 距離が0(頂点が1)が絶対に存在しないと駄目
    print(0)
    exit()
if D[0] != 0: # 頂点1が絶対に存在 距離が 0
    print(0)
    exit()
ans = 1
#print(dic)
for i in range(1,n):
    ans *= pow(dic[i-1],dic[i],mod)
    ans %= mod
print(ans)
