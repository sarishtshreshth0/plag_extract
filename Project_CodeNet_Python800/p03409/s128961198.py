def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()
def rand_N(ran1, ran2):
    return random.randint(ran1, ran2)
def rand_List(ran1, ran2, rantime):
    return [random.randint(ran1, ran2) for i in range(rantime)]
def rand_ints_nodup(ran1, ran2, rantime):
  ns = []
  while len(ns) < rantime:
    n = random.randint(ran1, ran2)
    if not n in ns:
      ns.append(n)
  return sorted(ns)

def rand_query(ran1, ran2, rantime):
  r_query = []
  while len(r_query) < rantime:
    n_q = rand_ints_nodup(ran1, ran2, 2)
    if not n_q in r_query:
      r_query.append(n_q)
  return sorted(r_query)

from collections import defaultdict, deque, Counter
from sys import exit
from decimal import *
import heapq
from math import sqrt, pi
from fractions import gcd
import random
import string
import copy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

N = getN()
# Rはループさせるのでソートさせる必要ない
R = [getList() for i in range(N)]
R_l = [1] * N

B = [getList() for i in range(N)]
B.sort()

# 貪欲法でペア作りする問題
# ABC005 C - おいしいたこ焼きの売り方の時と同様に
# それとしか繋げないもの　を優先的に繋いでいく

# 条件Aの通過が厳しい順に対象bをソートし、
# たこ焼き　条件A:客が来る前にたこ焼きができてないといけない
#  　　　　      客を来るのが早い順に並べる（最初から並んでる）
# 今回     条件A:赤星のx座標が青星のx座標より小さくないといけない
#  　　　　　　　 青星をx座標が小さい順に並べる

# 条件A, 条件Bをクリアしたものの中で、最も条件Bの通過が厳しい対象aと結ぶ
# たこ焼き　条件B:たこ焼きが賞味期限より前のものでないといけない
#  　　　　      できるだけ古いものを売る（最初から並んでる）
# 今回     条件B:赤星のy座標が青星のy座標より小さくないといけない
#  　　　　　　　 条件をクリアしたもののうちでできるだけy座標が大きいものを選ぶ

ans = 0
for b in B:
    max_y = -1
    max_index = -1
    for i, a in enumerate(R):
        # x, y座標が小さいもののうちでまた使ってないもの
        if a[0] < b[0] and a[1] < b[1] and R_l[i] == 1:
            # あるならY座標が最も大きいもの
            if a[1] > max_y:
                max_y = a[1]
                max_index = i
    if max_y >= 0:
        R_l[max_index] = 0
        ans += 1
print(ans)