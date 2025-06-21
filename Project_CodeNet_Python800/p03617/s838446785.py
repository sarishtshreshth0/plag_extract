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
mod = 10**9 + 7

def readInts():
  return list(map(int,input().split()))
def main():
    q,h,s,d = readInts()
    n = int(input())
    # 2A < B なら 0.25 のみ
    # 2A > B なら　0.5 のみ。
    # "入力は整数であるから、小数点を考える必要がない"
    # よって、0.25 -> 1, 0.5 -> 1 として、かつ1と比較する
    one = min(q*4, h*2, s)
    # そして、1gだけで行けるか、
    # 2gだけで買えるだけ買って、余った分を1gでやる
    print(min(one*n, d*(n//2) + one * (n%2)))#n//2 は 2g ずつなので、 n%2 は1gするか

if __name__ == '__main__':
  main()
