import math
import fractions
import heapq
import sys
import re
from collections import Counter
import datetime
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

#N,K=map(int, input().split())  #複数数値入力　「A B」みたいなスペース空いた入力のとき
#x=list(map(int, input().split()))  #リスト入力 「a1 a2 a3 ...」みたいな配列のような入力のとき

N=int(input())
print((2*N)//fractions.gcd(2,N))